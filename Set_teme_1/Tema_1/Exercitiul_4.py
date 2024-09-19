numar = input("Introduceti numarul: ")
este_numar = True
numar_negativ = False
if numar[0] == '-':
    numar_negativ = True
    numar = numar[1:] #atentie stringul e imutabil
for caracter in numar:
    if caracter < '0' or caracter > '9':
        este_numar = False
        break
if este_numar:
    numar = int(numar)
    if not numar_negativ:
        if numar < 10 and numar != 0:
            print('Numarul este mai mic decat 10.')
        elif numar == 0:
            print("Numarul este 0.")
        elif numar >= 10:
            print("Numarul nu se incadreaza in categoriile evaluate.")
    elif numar_negativ:
        print(f'Numarul pozitiv este {numar}')
else:
    print('Formatul numarului este invalid!')