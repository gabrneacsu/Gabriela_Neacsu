#contin doar elem unice
setul = {}
print(type(setul)) #asa tipul e dictionar
# solutie
setul = set()

setul = {1, 4, "item 1"}
setul.add(5)
setul2 = {4, 5, 2}
print(setul - setul2)
print(setul.union(setul2))
print(setul.intersection(setul2))