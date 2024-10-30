# pandas e o biblioteca fundamentala in python pt manipulare si analiza de date
# in machine learning iar pt manipulare date, inainte de procesul de modelare, datele trebuie standardizate, curatate

# seria - structura de date din pandas, unidimensionala, contine etichete cu scop de accesare a datelor (echivalenta cu lista din python)
# fiecare elem al seriei are o cheie asociata numita index (indexul e implicit sau se poate specifica manual)

import pandas as pd
import numpy as np
import datetime
# # pot crea o serie in pandas din:
# #a. din lista
# lista =  [10, 20, 30, 40, 50]
# serie = pd.Series(lista)
# print(serie)
# #atentie! fisierele nu se denumesc la fel cu bibliotecile

# #b. din array NumPy
# array_date = np.array([10, 20, 30, 40, 50])
# serie = pd. Series(array_date)
# print(serie)
# # lista ocupa mai mult decat un numpy - de aceea se foloseste pandas si numpy in procesarea de date

# #c. din dictionar
# dict_date = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# serie = pd.Series(dict_date)
# print(serie)

# cum adaug chei si in liste?
# lista =  [10, 20, 30, 40, 50]
# lista =  [10, 40, 20, 30, 50]
# eticheta = ['a', 'b', 'c', 'd', 'e']
# serie = pd.Series(lista, index = eticheta)
# print(serie)
# # daca vreau etiichetare implicita cu 0, 1.. nu specific indexul (varianta a.)
# # utilitate cand doresc sa accesez o valoare
# print(serie['b'])
# print(serie[['b', 'c', 'e']]) #evit asa sa fac un for prin seria respectiva ca sa gasesc o anumita eticheta
# print(serie['b': 'd']) #interval
# print(serie[1: 4]) #in continuare pot folosi indecsii, chiar daca am etichete
# print(serie[serie > 20])

# datetime e o librarie care ne ajuta sa formatam sub  forma de data timp o valoare si sa verif daca valoarea e corecta
# data_Si_timp = [datetime.datetime(2024, 1, 21),
#                 datetime.datetime(2024, 2, 22),
#                 datetime.datetime(2024, 3, 28)]
# ser_temporala = pd.Series([10, 20, 40], index=data_Si_timp)
# print(ser_temporala['2024-03-28'])
# # utila cand am un tabel de salarii, vanzari etc si vreau sa vad valoarea de la o anumita data la alta, adt tabelul initial trebuie sa fie sortat
# print(ser_temporala['2024-02-22': '2024-03-28']) #inainte sa pot face asta, datele alea trebuie sortate

# dataframe ul e tot tabelul, seria e o linie din tabel, (= structura bidimensionala)
# un data frame se poate realiza din:
# a. din dictionar
# data = {'Nume': ['ana', 'bogdan', 'cristina'],
#         'varsta': [25, 30, 32],
#         'salariul': [50000, 60000, 20000]}
# df = pd.DataFrame(data)
# print(df)
# caract dataframe uri: organizate in 2 dimensuni, are seturi de randuri si coloane
# nume = df['Nume']
# print(nume)
# salariu_bogdan = df.at[1, 'salariul']
# print(salariu_bogdan)
# pe data frame putem sa aplicam filtrare, functii, fara sa folosim for uri
# aici pot gestiona eficient lipsa unor date, le pot inlocui oricand cu o valoare sau sa excludem randul respectiv
# permite gruparea datelor
# df['experienta'] = [2, 5, 1]
# print(df)
# print(df.loc[1]) #accesez pe baza indexului daca nu am setat eu o eticheta specifica
# df.set_index('Nume', inplace=True) #daca vreau sa fac numele eticheta; inplace transmite toate modif in dataframe ul original
# print(df.loc['bogdan'])
# print(df.loc[1]) #daca setez o eticheta noua nu mai pot accesa pe baza indexului
# print(df.iloc[1]) #localizare pe baza de index, chiar daca am schimbat eticheta

# df_filtrat = df[df['varsta'] > 25]
# df_filtrat = df[df['salariul'] > 40000]
# print(df_filtrat)
# df_filtrare = df[(df['varsta'] > 25) & (df['experienta'] > 1)]
# print(df_filtrare)
# df_sortat = df.sort_values(by='varsta', ascending=False)
# print(df_sortat)
# df.set_index('Nume', inplace=True)
# df_sortat_index = df.sort_index()
# print(df_sortat_index)

# data = {'Nume': ['Ana', 'Bogdan', 'Ana', None, 'Cristina', 'Andrei', 'David', 'Ana'],
#         'Varsta': [25, 30, 25, 23, 22, 24, 35, None],
#         'Salariu': [50000, 60000, 60000, None, 10000, 450000, 70000, 50000]}
# #  NaN = Not a number
# df = pd.DataFrame(data)
# print(df)
# print('======================================')
# # df_fara_duplicate = df.drop_duplicates(subset=['Nume', 'Varsta'])
# # print(df_fara_duplicate)
# df.dropna(inplace=True) #elimina toate randurile care au valori de tip NaN
# # df.fillna(0, inplace=True) #dar strica statistica, de aceea e f imp procesul de curatare a datelor, datele lipsa se elimina sau se umplu cu info relevante
# df['Experienta'] = [3, 2, 4, 5, 2, 6] #nr de randuri trebuie sa coresp cu nr de val adaugate
# # df.rename(columns={'Experienta': 'NrAnDeMunca', 'Nume': 'Numele'}, inplace=True)
# df['Departament'] = ['IT', 'HR', 'IT', 'Vanzari', 'IT', 'HR']
# print(df)
# grupuri_departamente = df.groupby('Departament')
# for nume_departament, grup in grupuri_departamente:
#     print(f"\nGrupul pentru departamentul: {nume_departament}")
#     print(grup)
#
# medie_salarii = grupuri_departamente['Salariu'].mean()
# print('\nMedia salariilor pentru fiecare departament:')
# print(medie_salarii)
#
# rezultate_agregare = grupuri_departamente.agg({'Varsta': 'mean', 'Salariu': ['sum', 'median'], 'Nume': 'count'})
# print(rezultate_agregare)
#

# df1 = pd.DataFrame({'Nume': ['Ana', 'Bogdan'], 'Varsta': [25, 30]})
# df2 = pd.DataFrame({'Nume': ['Cristina', 'David'], 'Varsta': [22, 35]})
# df_concatenare_randuri = pd.concat([df1, df2], ignore_index=True) #Nu elimina duplicatele
# print(df_concatenare_randuri)
#
# df1 = pd.DataFrame({'Nume': ['Ana', 'Bogdan'], 'Varsta': [25, 30]})
# df2 = pd.DataFrame({'Salariu': [50000, 60000], 'Experienta': [2, 5]})
# df_concatenare_coloane = pd.concat([df1, df2], axis=1)
# print(df_concatenare_coloane)
#
# df1 = pd.DataFrame({'ID': [1, 2, 4], 'Nume': ['Ana', 'Bogdan', 'Cristina']})
# df2 = pd.DataFrame({'ID': [2, 3, 4], 'Salariu': [60000, 40000, 50000]})
# df_concatenare = pd.merge(df1, df2, on='ID', how='inner') #este ca un join, cu inner specific ca pastrez randurile cu id urile comune
# print(df_concatenare)
#
# df1 = pd.DataFrame({'Nume': ['Ana', 'Bogdan'], 'Varsta': [25, 30]}, index=[1, 2])
# df2 = pd.DataFrame({'Salariu': [50000, 60000], 'Experienta': [2, 5]},  index=[2, 3])
# df_imbinat_index = df1.join(df2, how='inner')
# print(df_imbinat_index)


data = {'Nume': ['Ana', 'Bogdan', 'Ana', None, 'Cristina', 'Andrei', 'David', 'Ana'],
        'Varsta': [25, 30, 25, 23, 22, 24, 35, None],
        'Salariu': [50000, 60000, 60000, None, 10000, 450000, 70000, 50000]}
df = pd.DataFrame(data)
df.dropna(inplace=True)
df['Departament'] = ['IT', 'HR', 'IT', 'Vanzari', 'IT', 'HR']
# print(df)
df.to_csv('date.csv', index=False) #modalitate de scriere in csv
df = pd.read_csv('date.csv') #modalitate de citire dintr-un csv
print(df)



