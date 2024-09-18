nr1 = 4
total, salariu = None, "Salariu mic"
print(salariu)
if nr1 <= 4 and (salariu := "salariu mare"):
    # asigneaza variabilei salariu valoarea salariu mare (pot folosi aceasta variabila strict in interiorul acestui bloc)
    # utila cand avem nevoie de anumite valori temporar
    total = nr1 + 1
elif nr1 < 2:
    total = nr1 + 2
# else:
#     total = None
# nepractica, mai bine declar la inceputul conditionarii

print(total)
print(salariu) #e folosibila doar daca e adev ce am in interiorul conditionarii (cel mai bine e sa pun o val default la fel ca la total)
