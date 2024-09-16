# print("Hello")  # comentariu
# print(3, type(3))
# print(2.4, type(2.4))
# print(3+1j, type(3+1j))
# print(int(3.5))
# print(float(4))
# print(3 * 5.4)
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(5 ** 2)
# print(5 == 5)
# print(5 != 5)
# print(5 > 5)
# print(5 >= 5)
# print(5 > 4 and 3 > 2)
"""
    operatorul AND
    true and true => true
    t and f => f
    f and t => f
    f and f => f
"""
# print(4 < 5 or 3 < 4)
"""
    oper OR
    t or t t
    t or f t
    f or t t
    f or f f
"""
# print(not(4 < 5))
"""
    oper negare
    true => false
    false => true
"""
# print("a" in "python") #operator de aparteneta (case sensitive)
# a = 1 #literele mari sunt pt denumirea de clase, deci la variabile se rec sa den var cu litera mica
# variabila_1 = None #cand vreau sa declar o var si nu vreau sa ii atribui o valoare (util pt for sau if de ex)
# print(variabila_1)
nr_mere = 2
nr_pere = 4
# variabila = 'Ana are ' + str(nr_mere) +' mere' #modalitate concatenare din python 2
# variabila = f"Ana are {nr_mere} mere si {nr_mere} pere" #functia f string, formateaza stringuri, ea convertese automat
variabila = "Ana are {0} mere si {1} pere".format(nr_mere, nr_pere)
print(variabila)
variabila = "Ana are {0} mere si {0} pere".format(nr_mere)
print(variabila)
variabila = "Ana are \"{}\" mere si \"{}\" pere".format(nr_mere, nr_pere)
variabila = 'Ana are "{}" mere si \n"{}" \tpere'.format(nr_mere, nr_pere)
print(variabila)