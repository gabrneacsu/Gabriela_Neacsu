"""scrieti un program care sa extraga inversul dintr-un nr.
Exemplu: 7536 trebuie afisati 6 3 5 7"""

numar = input('numar = ')
# print(numar[::-1]) #met 1

# met 2
new_number = ''
for i in numar:
    new_number = i + new_number #daca era new_number = new_number + i => afisa in aceeasi ordine
print(new_number)