"""
Sprint 1: Weerstation (console)
- Maximaal 7 dagen invoer
- Lege invoer stopt direct
- Robuuste validatie + duidelijke foutmeldingen
- Beslisregels exact volgens opdracht
"""

def fahrenheit(temp_celcius: float) -> float:
    return 32 + 1.8 * temp_celcius

def gevoelstemperatuur(temp_celcius: float, windsnelheid: int, luchtvochtigheid: int) -> float:
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid

def weerrapport(temp_celcius: float, windsnelheid: int, luchtvochtigheid: int) -> str:
    gt = gevoelstemperatuur(temp_celcius=temp_celcius, windsnelheid=windsnelheid, luchtvochtigheid=luchtvochtigheid)
    
    if gt < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gt < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= gt <= 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= gt <= 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= gt < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"

def exit_function() -> None:
    print("Aan het stoppen...\n")
    exit(0)

def weerstation() -> None:
    temp_per_dag = []
    i = 0
    while i < 7:
        print(f"---------- Dag {i+1} ----------")
        try:
            temp_celcius = input("Temperatuur (in graden Celcius): ")
            if temp_celcius.strip() == "":
                exit_function()
            temp_celcius = float(temp_celcius)

            windsnelheid = input("Windsnelheid (in meter/seconden): ")
            if windsnelheid.strip() == "":
                exit_function()
            windsnelheid = int(windsnelheid)
            if windsnelheid < 0:
                raise Exception("Windsnelheid ValueError")
            
            luchtvochtigheid = input("Luchtvochtigheid (in procenten): ")
            if luchtvochtigheid.strip() == "":
                exit_function()
            luchtvochtigheid = int(luchtvochtigheid)
            if luchtvochtigheid > 100 or luchtvochtigheid < 0:
                raise Exception("Luchtvochtigheid ValueError")
                        
            print(f"Vandaag was het {temp_celcius}C, {fahrenheit(temp_celcius=temp_celcius)}F")

            print(weerrapport(temp_celcius=temp_celcius, windsnelheid=windsnelheid, luchtvochtigheid=luchtvochtigheid))

            temp_per_dag.append(temp_celcius)

            gem = sum(temp_per_dag) / len(temp_per_dag)
            print(f"Gemiddelde temperatuur van laatste {len(temp_per_dag)} dag(en): {round(gem, 1)}\n")
            
            i += 1

        except ValueError:
            print("Je invoer moet een getal zijn...\n")
            continue

        except Exception as e:
            if e.args[0] == "Windsnelheid ValueError":
                print("Windsnelheid kan niet negatief zijn...\n")
                continue
            elif e.args[0] == "Luchtvochtigheid ValueError":
                print("Luchtvochtigheid moet een procent zijn, dus tussen de 0 en 100 liggen...\n")
                continue

if __name__ == "__main__":
    weerstation()
