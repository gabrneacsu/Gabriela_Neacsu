# face o lista de tupluri din 2 liste, in fct de pozitie
# lista_intregi = [1, 2, 3, 4, 5]
# lista_stringuri = ('unu', 'doi', 'trei', 'patru', 'cinci', 'sase')
#
# rezultat = list(zip(lista_intregi, lista_stringuri))
# print(rezultat)

# utila la cnp cand aveam calculul cifrei de control
cifra_de_control = 13433434
cnp = 12345678
print(list(str(cifra_de_control)))
rezultat = 0
for x, y in list(zip(list(str(cifra_de_control)), list(str(cnp)))):
    rezultat = int(x) * int(y) + rezultat
print(rezultat)