print('Meniu:\n1 – Afisare lista de cumparaturi\n2 – Adaugare element\n3 – Stergere element\n4 – Sterere lista de cumparaturi\n5 - Cautare in lista de cumparaturi ')
selectie = input("Alegeti o optiune: ")
if selectie == '1':
    print('Afisare lista de cumparaturi')
elif selectie == '2':
    print('Adaugare element')
elif selectie == '3':
    print('Stergere element')
elif selectie == '4':
    print('Sterere lista de cumparaturi')
elif selectie == '5':
    print('Cautare in lista de cumparaturi')
else:
    print('Alegerea nu exista. Reincercati')