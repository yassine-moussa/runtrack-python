def my_long_word(n, texte):
    mots = texte.split(" ")
    mots_long = []

    for mot in mots:
        longueur_mot = 0
        
        for lettre in mot:
            longueur_mot += 1
        
        if longueur_mot > n:
            mots_long.append(mot)

    resultat = " ".join(mots_long)
    return resultat

texte = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
n = 3
longs_mots = my_long_word(n, texte)
print("Mots plus longs que", n, "caractères :", longs_mots)
