from tempfile import tempdir

nb=int(input("quel est le nb de velo que vous voulez louer"))
h1=int(input("debut"))
h2=int(input("fin"))
a=0
if h1 > 0 and h2 < 24:

    if h1 <= h2:
        if h2 <= 7:
            a=  nb * (h2-h1)
            print(a)
        elif h2 > 7:
            a=(nb * (h2-h1))*2
            print(a)
    else:
        print("Attention ! l’heure de fin est identique à l’heure de début")
        print("Attention ! le début de la location est après la fin .")

else:
    print(" Les heures doivent être comprises entre 0 et 24")