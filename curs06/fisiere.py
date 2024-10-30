"""
r -> citire a fisierului, dar daca el nu exista, nu il adauga, daca nu ecista fisierul, apare eroare
w -> scriere in fisier, daca fisierul nu , il adauga
    dar daca exista informatie in fisier deja scrisa, w rescrie informatia
a -> modul append, scriere, daca exista informatia in fisier, ea nu se rescrie, a functioneaza ca un write, daca fisierul nu exista, nu e probl
r+ -> scrie, citeste, dar daca fisierul nu exista, apare eroare
"""
# file = open('nume_fisier.txt', 'r') #(denumire fisier, optional modul de deschidere a fisierului - r e default daca nu specific)
# file = open('nume_fisier.txt', 'w')
# file.write('hello\n')
# file.write('hello1\n')
# file.close()

# with open('nume_fisier.txt', 'w') as file: #creaza o var temporara numita file pe care o foloseste doar in int with ului
#     file.write('hello2')

# with open('nume_fisier1.txt', 'r') as file: #cu with fisierul se inchide automat cand iese din instructiune
#     text = file.readlines()
#     print(text)
#     for line in text:
#         print(line)

# with open('nume_fisier.txt') as variabila:
    # print(list(variabila)) #daca scriu asta nu mai interpreteaza for-ul, pt ca isi pierde continutul
    # for line in list(variabila):
    #     print(line)
    # #alternativa:
    # print(type(variabila))
    # a = list(variabila) # continutul treb pus intr-o var pt a functiona mai departe
    # print(a)
    # for line in a:
    #     print(line)


with open('nume_fisier.txt', 'r') as variabila:
    while True:
        line = variabila.readline()
        if not line:
            break
        print(line)