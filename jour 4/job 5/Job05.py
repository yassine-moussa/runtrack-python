def liste_entiers():
    L = [3, 6, 9, 12, 15]
    return L

def remplace(L):
    L[3] = L[2] + L[4]
    return L

L = liste_entiers()
print(L[1])

L = remplace(L)
print(L[-1])
