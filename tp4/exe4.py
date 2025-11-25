L1 = [2, 7, 5, 6, 7, 1, 6, 2, 6, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * """
cpt_max = 0
chiffre_max = 0

for chiffre in L1:
    cpt = 0
    for i in range(len(L1)):
        if L1[i] == chiffre:
            cpt += 1
    if cpt > cpt_max:
        cpt_max = cpt
        chiffre_max = chiffre

print(f"On a {cpt_max} fois : {chiffre_max}...")


