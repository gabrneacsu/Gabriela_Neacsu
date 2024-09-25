lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista_asc = lista

for i in range(len(lista_asc)-1):
    for j in range(len(lista_asc)-i-1):
        if lista_asc[j] < lista_asc[j+1]:
            lista_asc[j], lista_asc[j+1] = lista_asc[j+1], lista_asc[j]
print(f'Lista ascendenta este: {lista_asc}')
print(f'Lista descendenta este: {lista_asc[::-1]}')




