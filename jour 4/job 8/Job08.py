def somme_valeurs_paires(liste):
    somme = 0
    for element in liste:
        if element % 2 == 0:
            somme += element
    return somme

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
somme_des_paires = somme_valeurs_paires(L)
print("Somme des valeurs paires :", somme_des_paires)
