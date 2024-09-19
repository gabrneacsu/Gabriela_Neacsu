numar = input("Introduceti numarul: ")
este_numar = True
for caracter in numar:
    if caracter < '0' or caracter > '9':
        este_numar = False
        break
if este_numar:
    numar = int(numar)
    if numar % 2 == 0:
        print('Numarul este par.')
    elif numar % 2 == 1:
        print("Numarul este impar.")
else:
    print("Atentie, formatul numarului este gresit!")