def produit_valeurs_interval(liste, debut, fin):
    produit = 1
    for element in liste:
        if debut <= element <= fin:
            produit *= element
    return produit

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit_interval = produit_valeurs_interval(L, 25, 90)
print("Produit des valeurs dans l'intervalle [25, 90] :", produit_interval)
