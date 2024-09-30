text = input('adauga un nr:')
# conversie = int(text)
try:
    conversie = int(text)
    variabila
except ValueError: #daca are o eroare la ce e pe try, executa ce e pe exceptie
    print('exceptie de valoare')
except NameError:
    variabila = None
    print('Variabila a fost definita')
except Exception: #se trece mereu ultimul
    print('exceptie generala')
else: #executa cand pe try nu e eroare
    print(conversie)
finally: #util pt cand vrem sa inchidem fisiere
    print('se executa oricand')

print(conversie) #recomandat sa il def inainte, ca daca pe try e eroare, nu o sa fie definit