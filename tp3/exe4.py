nb=int(input("entrer un nombre"))
a=int(input("choisir 1 pour la boucle for et 0 pour la boucle while"))
b=0

if a == 0:
    while a < nb:
        b = b + 1
        a = a + b

    print(b)
else:
    for i in range(nb):
        b=b+1
        a=a+b

    print(a)