# my_numbers = {2, 4, 3, 5, 4, 1, 2}
# print(type(my_numbers))
# doubled = len(my_numbers) * 2
# print(doubled) #afiseaza 10 ca seturile afiseaza doar elementele unice, iar lungimea e cate elemente unice are setul

# var_1 = [x for x in range(20) if x / 2 == 0]
# print(var_1) # afis 0 ca e catul!!! nu restul

# char = 'cha'
# cha = 'char'
# print(len(char) * 'cha') #chachacha inmulteste stringul de cate ori e nr ul

# new_str = "Py'th\\'on"
# print(new_str[::-1]) #\ face escape pana la urm caracter, chiar daca e acelasi caracter

# planets = [['Mercury', 'Venus', 'Earth'],
#            ['Mars', 'Jupiter', 'Saturn'],
#            ['Uranus', 'Neptune', 'Pluto']]
# flatten_planets = []
# for sublist in planets:
#     for planet in sublist:
#         if len(planet) < 6:
#             flatten_planets.append(planet)
# print(flatten_planets)

# var_1 = ['abc', 'def', 'ghi']
# for item in var_1:
#     if type(item) == 'str':
#         item.upper() #atentie, el face upper, dar nu il inlocuieste in lista initiala asa cum am scris noi
#     else:
#         item.title()
# print(var_1)
# print('abc def'.title()) #rez: Abc Def
# print('abc def'.capitalize()) #rez: Abc def


# #modalitate desfasurata de scriere
# def double_number(n):
#     return lambda x: x * n
# result = double_number(5)
# #modalitate restransa de scriere
# result = lambda x: x * 5
# print(result(3-1))

# new_dict = {'item_1': 2, 'item_3': 1, 'item_2': 3}
# result = list(new_dict.keys()) + list(new_dict.values())
# print(str(result))

# def new_function(x, y) -> str:
#     new_result = x * 2 + y
#     if new_result % 2 != 0:
#         print('not even')
#     else:
#         return 'orice'
# print(new_function(2, 3))
# # rezultat not even\n none (ca o data printeaza ce e in functie si apoi returneaza none ca nu poate returna ce i am zis eu, ca e doar pe else

# def function_1():
#     print('variabila definita cu valoare', var)
# var = 10
# function_1()
# print(var)

# var_obj = {'key_1': 'val_1', 'val_2': 'key_2', 'key_3': 'val_3'}
# var_obj['key_2'] = 'val_2' #daca elem nu exista, adauga el
# #sau
# var_obj.update({'key_2': 'val_2'})
# print(var_obj)

# try:
#     value = int('test')
# except Exception as e:
#     print(e)

# new_list = list(set([1, 4, 5, 4, 2, 6, 3]))
# print({1, 4, 2, 6, 3, 8, 11, 2, 4, 8, 7})
# print(new_list)
# del(new_list[1: 6])
# print(new_list[-1])

# text_var = 'Python skills'
# try:
#     if 'py' in text_var:
#         print('Python')
# except Exception as e: #imi intoarce rezultatul exceptiei, e este temporar si imi da tipul eroarei
#     print('skills')
# else: # se executa else ul pt ca try ul nu genereaza nicio exceptie, daca try ul ar fi generat o exceptie (eroare), atunci s-ar fi afisat skills
#     print('execute')
# finally: #finally sigur se executa mereu, indiferent daca functuoneaza try ul sau nu
#     print('pass')

def my_function():
    l = list()
    for i in range(1, 4):
      l.append(i**2) # i**2 inseamna i la puterea 2
    return l
print(my_function())
