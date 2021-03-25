lista1 = [1, 2, 3, 4]
lista2 = [5, 7, 8, 9]

def unir(lista1, lista2):
    lista3 = list(set(lista1+lista2))
    return lista3

print(unir(lista1, lista2))