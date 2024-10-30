var = 'comprehension'
# print(list(var))
## alternativa 1
# list_for_loop = []
# for caracter in var:
#     list_for_loop.append(caracter)
# print(list_for_loop)
## alternativa 2
# list_for_loop = [caracter for caracter in var] #ce adaug in lista scriu in stanga inainte de for
# print(list_for_loop)
## alternativa 3

# numbers_list = []
# for x in range(30):
#     if x % 2 == 0:
#         numbers_list.append(x)
# print(numbers_list)

# #alternativa
# dictionar = {1: 1, 2: 4, 3:9}
# note_matem = {"ana": 5, "ion": 4, 'maria': 9}
# numbers_list = [x if y < 5 else 'a trecut' for x, y in note_matem.items()] #conditiile fara else in dreapta, ce vrem sa afisam in stanga
# # numbers_list = [x for x, y in note_matem.items() if y < 5] #conditiile fara else in dreapta, ce vrem sa afisam in stanga
# # numbers_list = [x for x in dictionar if x % 2 == 0] #conditiile fara else in dreapta, ce vrem sa afisam in stanga
# # numbers_list = [x for x in range(30) if x % 2 == 0] #conditiile fara else in dreapta, ce vrem sa afisam in stanga
# print(numbers_list)

# dictionar = {}
# for i in range(1, 11):
#     dictionar[i] = i*i
# print(dictionar)
# alternativa
dictionar = {i: i*i if i % 2 == 0 else 0 for i in range(1, 11)} #ca sa il fac dictionar i: i*i
# dictionar = {i: i*i for i in range(1, 11) if i % 2 == 0} #ca sa il fac dictionar i: i*i
print(dictionar)

