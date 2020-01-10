annee=0
annee = int(annee)
annee=input("Saisissez une annee: ")
if annee % 4 != 0:
    print("Cette annee n'est pas une annee bissextille")
elif annee % 4 == 0 and annee % 100 == 0:
    print("Cette annee est bien une anne bissextile")
else:
    print("Cette annee n'est pas une annee bissextille")
