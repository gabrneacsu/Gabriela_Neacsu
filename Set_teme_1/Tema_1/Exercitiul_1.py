nume_utilizator = input("Numele meu este: ")
text_introdus = input("Introduceti textul: ")
este_numar = True
for caracter in text_introdus:
    if caracter < '0' or caracter > '9': #sau if caracter not in '123456789'
        este_numar = False
        break
if este_numar and text_introdus != '':
    print('e numar')
elif text_introdus != '':
    print(f'Sirul de caractere a fost gasit de {nume_utilizator}')
else:
    print("Textul introdus este gol!")

