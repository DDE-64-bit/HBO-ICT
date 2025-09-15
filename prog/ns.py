def standaartPrijs(afstandKM: int) -> float:
    if afstandKM > 50:
        return 15 + 0.60 * afstandKM
    if afstandKM <= 0:
        return 0
    else:
        return 0.80 * afstandKM

def ritPrijs(leeftijd: int, weekendrit: bool, afstandKM: int) -> float:
    prijs = standaartPrijs(afstandKM)
    
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit:
            return prijs * 0.65
        return prijs * 0.7
    if weekendrit:
        return prijs * 0.6
    return prijs

if __name__ == "__main__":
    try:
        leeftijd = int(input("Wat is uw leeftijd?\n"))
        while True:
            weekendrit = input("Is dit een weekend rit (True/False)?\n")
            if weekendrit != "True" and weekendrit != "False":
                print("Het komt nog niet helemaal overeen, probeer het opnieuw...\n")
                continue
            weekendrit = bool(weekendrit)
            break
        afstandKM = int(input("Afstand in hele kilometers?\n"))

    except ValueError:
        print("Uw invoer is onjuist...")
        exit(1)

    print(ritPrijs(leeftijd, weekendrit, afstandKM))