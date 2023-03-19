def distance_parcourue(nb_marches, hauteur_marche_cm):
    
    hauteur_marche_m = hauteur_marche_cm / 100

    
    distance_aller_retour_m = 2 * nb_marches * hauteur_marche_m

    
    distance_semaine_m = 5 * distance_aller_retour_m * 7

    return distance_semaine_m

nb_marches = 100
hauteur_marche_cm = 20
distance_semaine_m = distance_parcourue(nb_marches, hauteur_marche_cm)
print(f"Pour {nb_marches} marches de {hauteur_marche_cm} cm, le gardien parcourt {distance_semaine_m:.2f} m par semaine.")
