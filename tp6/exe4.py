import random

def generer(nbr, vmin, vmax):
    table = []
    for _ in range(nbr):
        table.append(random.randint(vmin, vmax))
    return table

def combienInferieur(table, vseuil):
    compteur = 0
    for valeur in table:
        if valeur < vseuil:
            compteur += 1
    return compteur


# --- Programme principal interactif ---

# Demande du nombre de valeurs
nb = int(input("Combien de valeurs voulez-vous générer ? "))

# Demande des bornes
vmin = int(input("Valeur minimale (vmin) : "))
vmax = int(input("Valeur maximale (vmax) : "))

# Demande sur le seuil
rep = input("Vous voulez préciser le seuil ? (Oui/O ou Non/N) : ")

if rep.lower() in ["oui", "o"]:
    seuil = int(input("Entrez le seuil : "))
else:
    seuil = 30
    print("Seuil par défaut appliqué : 30")

# Génération et traitement
print(f"\nGénérer {nb} nombres entiers entre {vmin} et {vmax}...")
tab = generer(nb, vmin, vmax)

tab.sort()
print("Tableau trié :")
print(tab)

total = combienInferieur(tab, seuil)
print(f"\nNombre de valeurs inférieures à {seuil} : {total}")
