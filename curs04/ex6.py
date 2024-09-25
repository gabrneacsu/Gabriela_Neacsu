"""
Scrieti un program care sa faca split dupa al n-lea element intr-o lista:

lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
result = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""
lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
lista_micuta = []
rezultat = []
a = len(lista_start)
for i in range(n):
    lista_micuta = []
    for j in range(a):
        if j % n - i == 0:
            lista_micuta.append(lista_start[j])
    rezultat.append(lista_micuta)

print(rezultat)
