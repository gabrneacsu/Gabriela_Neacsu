numar = input("Introduceti numarul: ")
rezultat = numar
if numar.isdigit():
    numar = int(numar)
    if numar % 3 == 0 and numar % 5 == 0:
        rezultat = 'FizzBuzz'
    elif numar % 3 == 0 and numar % 5 != 0:
        rezultat = 'Fizz'
    elif numar % 3 != 0 and numar % 5 == 0:
        rezultat = 'Buzz'
print(rezultat)

# element.isdigit()
#       => True - daca caracterele din string sunt cifre
#       => False - altfel