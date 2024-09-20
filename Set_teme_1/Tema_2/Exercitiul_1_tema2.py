a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

intersectie = list((set(a)).intersection(set(b)))
print(intersectie)

# atentie! util de folosit seturile pentru ca in cazul listelor ele sunt ordonate si permit duplicate
# intersectia pe liste ar implica gestionarea duplicatelor si a ordinii