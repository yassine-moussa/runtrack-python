def arrondir_nombre(nombre):
    partie_entiere = int(nombre)
    decimal = nombre - partie_entiere
    if decimal >= 0.5:
        return partie_entiere + 1
    else:
        return partie_entiere

def tri_croissant(liste):
    n = 0
    for element in liste:
        n += 1

    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
nombres_arrondis = [arrondir_nombre(nombre) for nombre in nombres]
nombres_tries = tri_croissant(nombres_arrondis)
print("Liste arrondie et triée :", nombres_tries)
