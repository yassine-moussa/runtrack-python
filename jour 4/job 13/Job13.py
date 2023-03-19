def supprimer_doublons(liste):
    nouvelle_liste = []
    for element in liste:
        if element not in nouvelle_liste:
            nouvelle_liste.append(element)
    return nouvelle_liste

exemple_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste_sans_doublons = supprimer_doublons(exemple_liste)
print("Liste sans doublons :", liste_sans_doublons)
