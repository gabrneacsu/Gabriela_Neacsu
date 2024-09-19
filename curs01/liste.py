lista = [8, 2, 8, 'ana are mere', 4.2, True]
print(type(lista))
# recomandare sa avem acelasi tip de date in toata lista
# print(lista[0:1])
# print(len(lista))
# print(lista[2:8])
# print(lista[-1])
# print(lista[-6])
# print(lista[-6:])
# print(lista[-6:-3])
# print(lista[2:8:2]) #[poz_start:poz_stop:pas]
lista.append(5.6) #adauga la finalul listei
# print(lista.index(2)) #index(element) => pozitie (daca se repeta, atunci returneaza doar primul index/ pozitie)
# lista.remove(2) #sterge in functie de valoare
# # lista.pop()
# lista.pop(3) #sterge in fct de poz
# lista.clear()
# lista.reverse()
lista.pop(3)
lista.pop(4)
lista.sort() #doar daca au acelasi tip!! (poate sorta si daca ramane true in lista de integer, ca o ia ca 1, nu face diferenta dintre false si 0, respectiv 1 si true, le sorteaza in ordinea aparitiei daca sunt amandoua prezente)
print(lista)
