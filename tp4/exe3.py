nMax=3
v1=[]
v2=[]
n=int(input("quel est votre taille de veteur : "))
if n <= nMax and n >= 1:
    print("Saisie du premier vecteur :")
    for i in range(n):
        v1.append(int(input(f"v1[,{i}] = ")))
    print("Saisie du deuxième vecteur :")
    for i in range(n):
        v2.append(int(input(f"v2[{i}] = ")))

    for i in range(n):
        tot= v1[i] * v2[i]
    print("Le produit scalaire de v1 par v2 vaut ", tot)
else:
    n=int(input("entrer un nombre entre 1 et 3 : "))
