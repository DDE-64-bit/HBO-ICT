# """
# def kosten(boeken: int) -> int:
#     kosten = boeken * (24.95 *0.6)
    
#     boeken -= 1
#     if boeken >= 0:
#         kosten += 3
#     else:
#         exit(1)
    
#     kosten += boeken * 0.75
    
#     return kosten 

# if __name__ == "__main__":
#     try:
#         print(kosten(int(input("Aantal boeken: "))))
#     except ValueError:
#         print("Je moet een getal invullen...")
# """

# var1, var2, var3 = 10, 21, 31
# gemiddelde = (var1 + var2 + var3)/3

# print(f"gemiddelde: {round(gemiddelde, 3)}\n")

# maxVar = max(var1, var2, var3)
# minVar = min(var1, var2, var3)

# print(f"max: {maxVar}")
# print(f"min: {minVar}")

# print(f"gemiddelde: {round((maxVar+minVar)/2, 3)}")


# s1, s2, s3 = "Hogeschool Utecht", "Heidelberglaan", "programming"

# if "sch" in s1:
#     print("sch is in s1")
# else:
#     print("sch is niet in s1")

# if " " not in s2:
#     print("geen spaties in s2")
# else:
#     print("er zijn/is een of meerdere spaties in s2")

# print(s1+s2+s3)

# print(s2[12])





def name():
    try:
        naam = input("wat is je naam? \n")
        leeftijd = int(input("wat is je leeftijd? \n"))
    except ValueError:
        print("leeftijd moet een getal zijn...")
        exit(1)
    leeftijd_over_een_jaar = leeftijd + 1
    
    print(f"Welkom {naam}, nu ben je nog {leeftijd}. Maar over een jaar ben je {leeftijd_over_een_jaar}")

if __name__ == "__main__":
    name()