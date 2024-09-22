anul = input("Introduceti anul dorit: ")
format_corect_an = True
#verific daca ce am introdus de la tastatura este un integer (respectiv daca poate fi un an), sau un string
for caracter in anul:
    if caracter < '0' or caracter > '9':
        format_corect_an = False
        break
if format_corect_an:
    anul = int(anul)
    if (anul % 4 == 0 and anul % 100 != 0) or (anul % 400 == 0):
        print('Anul este bisect.')
    elif anul % 4 != 0:
        print("Anul nu este bisect.")
else:
    print("Atentie, formatul anului este invalid!")