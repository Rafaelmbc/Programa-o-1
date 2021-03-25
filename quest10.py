lista = []
for i in range(1, 101):
    lista.append(i)
print('Lista de Numeros de 1 a 100')
print(lista)

lista2 = [numero for numero in range(1, 101) if numero % 2 == 0]
print('Números pares de 1 a 100:')
print(lista2)

lista3 = [numero for numero in range(1, 101) if numero % 5 == 0]
print('Multiplos de 5:')
print(lista3)