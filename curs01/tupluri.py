# my_tuple = (1, 7, -3)
my_tuple = (1, 7, -3)
print(type(my_tuple))
print(list(my_tuple))
# nu ai cum sa schimbi tipul unui dictionar
my_tuple = (1)
print(my_tuple)
print(type(my_tuple)) # cu un elem ia tipul primului elem, nu mai e tuplu
# solutie
my_tuple = (1, )
print(type(my_tuple))