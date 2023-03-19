def echanger_valeurs(liste):
    if len(liste) > 1:
        liste[0], liste[-1] = liste[-1], liste[0]
    return liste

exemple = [1, 2, 3, 4, 5]
liste = echanger_valeurs(exemple)
print(liste)
