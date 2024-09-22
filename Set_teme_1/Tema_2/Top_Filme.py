lista_utilizatori = [
    {'nume': 'George', 'filme': ['Shrek', 'Bond', 'Fight Club']},
    {'nume': 'Cristian', 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']},
    {'nume': 'Stefan', 'filme': ['Fight Club', 'Slumdog Milionaire']}
]
#Rezolvare top filme
lista_filme_totala = lista_utilizatori[0].get('filme') + lista_utilizatori[1].get('filme') + lista_utilizatori[2].get(
    'filme')  #este o lista ce contine toate filmele vizionate de toti utilizatorii la un loc
element = element_aux = 'None'
i = j = 0
frecventa_maxima = 0
frecventa_filme = list()  #este o lista in care am frecventa aparitiei fiecarui film
nume_filme = list()  #o lista in care am filmul corespunzator cu nr de aparitii
#crearea celor doua liste, cu frecventa aparitiei si numele filmelor:
while lista_filme_totala:
    frecv_aux = 0
    element = lista_filme_totala[0]
    for element_aux in lista_filme_totala:
        if element == element_aux:
            frecv_aux += 1
    frecventa_filme.append(frecv_aux)
    nume_filme.append(element)
    while element in lista_filme_totala:
        lista_filme_totala.remove(element)
#sortarea in functie de frecventa filmelor
for i in range(len(frecventa_filme) - 1):
    for j in range(0, len(frecventa_filme) - i - 1):
        if frecventa_filme[j] < frecventa_filme[j + 1]:
            frecventa_filme[j], frecventa_filme[j + 1] = frecventa_filme[j + 1], frecventa_filme[j]
            nume_filme[j], nume_filme[j + 1] = nume_filme[j + 1], nume_filme[j]
print(f'Topul filmelor este: {nume_filme}')
print(f'Filmul cel mai vizionat este {nume_filme[0]} si este vizionat de {frecventa_filme[0]} ori')


#Rezolvare top utilizatori cu cele mai multe filme vizionate:
top_utilizatori_dict = {} #dictionarul va avea ca si cheie numele utilizatorului si ca si valoare nr de filme vizionate
for value in lista_utilizatori:
    top_utilizatori_dict[value.get('nume')] = len(value.get('filme'))

#crearea unor liste care contin numele utilizatorilor, respectiv nr filme vizionate
lista_nume = list(top_utilizatori_dict.keys())
lista_nr_filme = list(top_utilizatori_dict.values())  #asa pastreaza tipul anterior din dictionar, altfel ajungeau toate string

# sortarea utilizatorilor in functie de nr de filme vizionate
for i in range(len(lista_nr_filme) - 1):
    for j in range(0, len(lista_nr_filme) - i - 1):
        if lista_nr_filme[j] < lista_nr_filme[j + 1]:
            lista_nr_filme[j], lista_nr_filme[j + 1] = lista_nr_filme[j + 1], lista_nr_filme[j]
            lista_nume[j], lista_nume[j + 1] = lista_nume [j + 1], lista_nume[j]
print(f'Topul utilizatorilor este: {lista_nume}')
print(f"Utilizatorul cu cele mai multe filme vizionate este {lista_nume[0]}")

# mentiune, puteam sa rezolv si cerinta cu top utilizatori, si pe cea cu top filme cu dictionare, dar mi am dat seama dupa
