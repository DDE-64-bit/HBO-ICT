#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback, collections

"""
Programming
Opdracht PROG: NS-Functies
(c) 2024 Hogeschool Utrecht,
Bart van Eijkelenburg (bart.vaneijkelenburg@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.
"""


def standaardprijs(afstandKM: int) -> float:
    """
    Berekent de standaardprijs voor een NS-reis op basis van afstand.
    
    Args:
        afstandKM: Afstand in kilometers
        
    Returns:
        float: Prijs in euro's (0 voor negatieve of nul afstanden)
        
    Raises:
        TypeError: Als afstandKM geen numerieke waarde is
        ValueError: Als afstandKM onrealistisch hoog is
    """
    # Input type validatie
    if not isinstance(afstandKM, (int, float)):
        raise TypeError(f"afstandKM moet een numerieke waarde zijn, kreeg: {type(afstandKM).__name__}")
    
    # Controleer op NaN of infinity waarden
    if isinstance(afstandKM, float) and (afstandKM != afstandKM or afstandKM == float('inf') or afstandKM == float('-inf')):
        raise ValueError(f"afstandKM mag geen NaN of infinity zijn")
    
    # Realistische maximum afstand validatie (Nederland is ~300km lang)
    if afstandKM > 1000:
        raise ValueError(f"afstandKM te groot (max 1000km), kreeg: {afstandKM}")
    
    # Behandel negatieve of nul afstand als speciaal geval (voor backward compatibility)
    if afstandKM <= 0:
        return 0.0
    
    # Bereken prijs volgens NS-tariefstructuur
    if afstandKM > 50:
        return 15.0 + 0.60 * afstandKM
    else:
        return 0.80 * afstandKM


def ritprijs(leeftijd: int, weekendrit: bool, afstandKM: int) -> float:
    """
    Berekent de ritprijs inclusief kortingen op basis van leeftijd en weekendrit.
    
    Args:
        leeftijd: Leeftijd van de reiziger (0-150 jaar)
        weekendrit: True als het een weekendrit betreft
        afstandKM: Afstand in kilometers
        
    Returns:
        float: Prijs in euro's inclusief eventuele kortingen
        
    Raises:
        TypeError: Als parameters niet het juiste type hebben
        ValueError: Als parameters buiten redelijke ranges vallen
    """
    # Input type validatie
    if not isinstance(leeftijd, int):
        raise TypeError(f"leeftijd moet een integer zijn, kreeg: {type(leeftijd).__name__}")
    
    if not isinstance(weekendrit, bool):
        raise TypeError(f"weekendrit moet een boolean zijn, kreeg: {type(weekendrit).__name__}")
    
    if not isinstance(afstandKM, (int, float)):
        raise TypeError(f"afstandKM moet een numerieke waarde zijn, kreeg: {type(afstandKM).__name__}")
    
    # Input range validatie (redelijke grenzen)
    if leeftijd < 0 or leeftijd > 150:
        raise ValueError(f"leeftijd moet tussen 0 en 150 jaar zijn, kreeg: {leeftijd}")
    
    # afstandKM validatie wordt gedaan door standaardprijs functie
    if afstandKM > 1000:
        raise ValueError(f"afstandKM te groot (max 1000km), kreeg: {afstandKM}")
    
    # Bereken basisprijs (standaardprijs handelt negatieve waarden af)
    try:
        prijs = standaardprijs(afstandKM)
    except (TypeError, ValueError) as e:
        # Re-raise met meer context
        raise ValueError(f"Fout bij berekenen basisprijs: {str(e)}")
    
    # Pas kortingen toe op basis van leeftijd en weekendrit
    if leeftijd < 12 or leeftijd >= 65:
        # Kinderen onder 12 en senioren 65+ krijgen korting
        if weekendrit:
            return prijs * 0.65  # 35% korting in weekend
        else:
            return prijs * 0.7   # 30% korting doordeweeks
    else:
        # Volwassenen tussen 12-64 jaar
        if weekendrit:
            return prijs * 0.6   # 40% korting in weekend
        else:
            return prijs         # Geen korting doordeweeks


def development_code():
    pass


def module_runner():
    development_code()      # Comment deze regel om je 'development_code' uit te schakelen
    __run_tests()           # Comment deze regel om de HU-tests uit te schakelen


"""
==========================[ HU TESTRAAMWERK ]================================
Hieronder staan de tests voor je code -- daaraan mag je niets wijzigen!
"""


def __my_assert_args(function, args, expected_output, check_type=False):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output).__name__} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    if str(expected_output) == str(output):
        msg = f"Fout: {function.__name__}{argstr} geeft {output} ({type(output).__name__}) " \
              f"in plaats van {expected_output} (type {type(expected_output).__name__})"
    else:
        msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"

    if type(expected_output) is float and isinstance(output, (int, float, complex)):
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_standaardprijs():
    case = collections.namedtuple('case', 'distance expected_output')

    testcases = [ case(-51, 0), case(-10, 0), case(0, 0), case(10,8),
                  case(49, 39.2), case(50, 40), case(51, 45.6), case(80, 63) ]

    for test in testcases:
        __my_assert_args(standaardprijs, (test.distance,), test.expected_output)


def test_ritprijs():
    case = collections.namedtuple('case', 'age weekend distance expected_output')

    testcases = [ case(11, True,  50, 26.0),  case(11, False,  50, 28.0), case(11, True,  51, 29.64),
                  case(11, False, 51, 31.92), case(11, True, -51,  0.0),  case(11, False, -51,  0.0),
                  case(12, True,  50, 24.0),  case(12, False, 50, 40.0),  case(12, True,  51, 27.36),
                  case(12, False, 51, 45.6),  case(12, True, -51,  0.0),  case(12, False, -51, 0.0),
                  case(64, True,  50, 24.0),  case(64, False,  50, 40.0), case(64, True,  51, 27.36),
                  case(64, False, 51, 45.6),  case(64, True, -51,  0.0),  case(64, False, -51,  0.0),
                  case(65, True,  50, 26.0),  case(65, False, 50, 28.0),  case(65, True,  51, 29.64),
                  case(65, False, 51, 31.92) ]

    for test in testcases:
        __my_assert_args(ritprijs, (test.age, test.weekend, test.distance), test.expected_output)


def __run_tests():
    """ Test alle functies. """
    test_functions = [ test_standaardprijs, test_ritprijs ]

    try:
        for test_function in test_functions:
            func_name = test_function.__name__[5:]

            print(f"\n======= Test output '{test_function.__name__}()' =======")
            test_function()
            print(f"Je functie {func_name} werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as e:
        print(e.args[0])
    except Exception as e:
        print(f"Fout: er ging er iets mis! Python-error: \"{e}\"")
        print(traceback.format_exc())


if __name__ == '__main__':
    module_runner()