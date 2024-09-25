"""Se cer 2 nr intregi de la tastatura. Sa se calculeze produsul daca produsul dintre cele 2 numere este
mai mic sau egal cu 1000, altfel, sa se returneze suma acestora."""

a = input('a = ')
b = input('b = ')
# produs = suma = None #None este Null din alte limbaje de programare
rezultat = None
operatie = None
if a.isdigit() and b.isdigit():
    a, b = int(a), int(b)
    #produs = a * b
    if (rezultat:= a * b) and rezultat <= 1000: #sau if a * b: - aici fac alocaarea si verificarea in interiorul if-ului, e mai eficient (in acest caz produs are valori pt ca fac atribuirea inainte sa fac verificarea (Fara randul din ult else cand fac produs = none)
        operatie = 'produs'
    else:
        rezultat = a + b
        operatie = 'suma'
#folosesc o var produs in loc sa afisez direct pt ca daca nu, as calcula de 2 ori, si la if si la afisare

    print(f'{operatie}: {rezultat}')

