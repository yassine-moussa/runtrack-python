def maximum_minimum_valeurs(liste):
    max_val = liste[0]
    min_val = liste[0]
    for element in liste:
        if element > max_val:
            max_val = element
        if element < min_val:
            min_val = element
    return max_val, min_val

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
maximum, minimum = maximum_minimum_valeurs(L)
print("Maximum :", maximum)
print("Minimum :", minimum)
