# ia un iterabil si inlocuieste fiecare elem in functie
# def suma(x, y):
#     return x + y
#
# rezultat = suma(1, 2)
# print(rezultat)

# suma = lambda x, y: x + y #dezavantaj nu pot folosi pt lucruri mai complexe
# # avantaj ocupa locatie de memorei doar in timpul rularii, dar apoi e stearsa
# rezultat = suma(1, 2)
# print(rezultat)

jucatori = [{
    'nume': 'popescu',
    'prenume': 'ion',
    'varsta': 21
},
{
    'nume': 'Marin',
    'prenume': 'andreea',
    'varsta': 42
},
{
    'nume': 'ionescu',
    'prenume': 'maria',
    'varsta': 14
}]

sortare_valori = sorted(jucatori, key = lambda valoare: valoare['varsta'], reverse = True)
print(sortare_valori)

# sorted (lista de sortat, chei, optional reverse true ca sa afseze invers)
# implicit reverse e False, ca sa afiseze crescator

