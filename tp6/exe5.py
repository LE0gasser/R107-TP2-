chaine = input("Entrez un mot ou une phrase : ")

chaine_epuree = ""
for i in chaine:
    if i.isalpha():

        chaine_epuree += i.lower()


if chaine_epuree == chaine_epuree[::-1]:
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")
