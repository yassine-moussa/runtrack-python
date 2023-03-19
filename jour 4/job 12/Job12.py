def tri_ordre_croissant(liste):
    n = 0
 
    for element in liste:
        n += 1
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

liste = [34, 12, 5, 78, 24, 89, 2, 55]
liste_triee = tri_ordre_croissant(liste)
print("Liste triée :", liste_triee)
