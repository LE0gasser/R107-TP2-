a=0
b=0
c=0
for i in range(10):
    nb=int(input("quel est votre nb entre 0 et 20"))
    if nb >= 0 and nb <= 20:
        if nb < 10:
            a=a+1
        elif nb >= 10 and nb < 15:
            b=b+1
        else :
            c=c+1
    else:
        nb=int(input("il faut un nb entre 0 et 20"))
print("il y a",a,"nombre inferieur a 10 et il y a",b,"nombre superieur a 10 et inferieur a 15 et il y a ",c,"nombre superieur a 15")