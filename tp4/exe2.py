nbe = int(input("Donnez le nombre d'etudiants : "))
dif=0
moyenne = 0;
notes = []
for i in range(nbe):

    notes.append(int(input(f"quelles note a eu l'eleves  {i + 1} : ")))
moyenne=sum(notes)/nbe
print(f"la moyenne de classe est de {moyenne}")
dif = moyenne - notes
for i in range(nbe):
    print({i + 1} | {notes} | {dif})