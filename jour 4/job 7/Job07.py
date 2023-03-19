def multiples_de_trois(liste):
    compteur = 0
    for element in liste:
        if element % 3 == 0:
            compteur += 1
    return compteur

L = [8, 24, 48, 2, 16]
multiples_de_3 = multiples_de_trois(L)
print("Nombre de multiples de trois :", multiples_de_3)
