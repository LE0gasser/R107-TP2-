BASE=4
fromage=800.0
eau=2
ail=2
pain=400
nbconvives=int(input("Entrez le nombre de personne(s) conviées à la fondue :"))
print("Pour faire une fondue fribourgeoise pour ",nbconvives," personnes, il vous faut :")
fromage= fromage * nbconvives / BASE
eau = eau * nbconvives / BASE
ail = ail * nbconvives /BASE
pain =pain * nbconvives /BASE
print("-",fromage,"gr de fromage")
print("-",eau,"dl d'eau")
print("-",ail,"gousse d'ail")
print("-",pain,"gr de pain")