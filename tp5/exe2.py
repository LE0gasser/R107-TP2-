note = []
coef = 0
compt = 0
somme_notes = 0
somme_coef = 0

for i in range(5):
    txt_note = input(f"quel est la note {i+1} et quel est son coef? ")
    note_coef = txt_note.split(" ")

    note = int(note_coef[0])
    coef = int(note_coef[1])

    somme_notes += note * coef
    somme_coef += coef

moyenne = somme_notes / somme_coef
print(moyenne)

if moyenne > 10:
    print("admis")
else:
    print("non admis")
