
heures = float(input("Entrez le nombre d'heures travaillées : "))
salaire_h = float(input("Entrez le salaire horaire : "))


if heures <= 160:
    salaire = heures * salaire_h

elif heures <= 200:
    salaire = 160 * salaire_h \
              + (heures - 160) * salaire_h * 1.25

else:
    salaire = 160 * salaire_h \
              + 40 * salaire_h * 1.25 \
              + (heures - 200) * salaire_h * 1.50

# Affichage du résultat
print(f"Le salaire total est de : {salaire:.2f} euros")
