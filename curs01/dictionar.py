dictionar = {1: "Ana", "2": "Mere", "3": "Pere", 4: "prune", 1: "Antonia", "1": "andreea" }
# print(type(dictionar))
# print(dictionar["2"])
# print(dictionar["22"])
print(dictionar.get("22", "Nu gaseste nimic")) #dar nu asociaza cheia 22 care nu a existat cu valoarea "nu gaseste nimic"
# cheile pot fi cifre, litere, tupluri, boolene, etc
# ia ult valoare pt cheie, ca listele
# recomandare sa fie de acelasi tip valorile, cheile
# dictionar["22"] = "valaore noua"
# dictionar.update({"23": "alta valoare", "33": "extra"})
print(dictionar.keys())
print(dictionar.values())
print(dictionar.items())
# print(dictionar)
