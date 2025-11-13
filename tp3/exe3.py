import random

x = random.randint(0, 100)
i = 0

while True:
    user_input = int(input("entré une valeure entre 0 et 100"))
    i += 1
    if user_input == x:
        print("trouver")
        break
    elif user_input < x:
        print("le nombre est plus grand")
    elif user_input > x:
        print("le nombre est plus petit")
    elif user_input > 100 or user_input < 0:
        print("merci d'entré une valeur entre 0 et 100")

print("Le nombre de tentative est:", i)