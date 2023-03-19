def creer_liste_entier(liste, increment):
    for i, element in enumerate(liste):
        liste[i] = element + increment
    return liste

L = [7, 11, 42, 39, 2]
L_modifiee = creer_liste_entier(L, 1)
print("Liste modifiée :", L_modifiee)

