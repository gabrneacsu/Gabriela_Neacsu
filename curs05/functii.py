#  apelarea functiei:
# print('Ana') #den_fct(parametrii)
# input()
# ctrl B duce la codul functiei

# def functia_mea(param_1, param_2): #param de intrare in paranteze
#     # aici e namespace ul local al functiei
#     # e bine sa nu avem print uri in functie
#     return 'ana are mere', 'ana are mere' #param de iesire
#
# rezultat = functia_mea(1, 2)
# # ctrl P si vad denumirea parametrilor
# print(rezultat)

# in namespace ul global intai se defineste functia, apoi se apeleaza
# https://docs.python.org/3/library/functions.html


# # def suma(a: int, b: int) -> (int, int):
# def suma(c, a: int = 1, b: int = 2) -> (int, int): #dar e riscul la apel cand trec valorile param, de ex a sa aiba val c samd
def suma(a: int = 1, b: int = 2, c: int = 3, *args, **kwargs) -> (int, int):
    # **kwargs e dictionar, se scrie dupa args, daca folosim si args!!!
    # e bine sa def tipul param de intrare, dar nu obligatoriu
    # -> (int, int), modalitatea prin care ii zic tipul a ce iese
    # cand trecem valori default, e obligatoriu pt toti parametrii de intrare
    print(type(args)) #e tuplu args, e util pt valorile adaugate extra
    suma = a + b + c
    for i in args:
        suma = suma + i
    for i in kwargs.values():
        suma = suma + i
    return suma, a-b
#     util cand nu stiu cate val o sa am cand apelez functia, valorile din args se separa prin virgula la apelare

# rezultat = suma(1, 2)
# rezultat_suma, rezultat_diferenta = suma(1, 3) #pozitionali, oblogatoriu sa trec pt fiecare param valoarea la apelare
rezultat_suma, rezultat_diferenta = suma(1, 2, 3, 4, 5, 6, 7, 9, 10, d = 5, e = 6) #de tip cheie valoare, aici nu mai e obligatoriu sa trec pt fiecare param valoarea la apelare

print(rezultat_suma, rezultat_diferenta)
