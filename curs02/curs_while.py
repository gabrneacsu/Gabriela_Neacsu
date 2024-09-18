a = 10
while 1 < a <= 10:
    print(f"Ana are {a} mere")
    if a % 2 == 0:
        continue #nu mai executa nimic din condul de mai jos, ci se intoarce la conditia de while de sus
    a -= 1 #a = a - 1 (echivalent)
    # break #este o iesire fortata, ajuta cand e bucla infinita
    