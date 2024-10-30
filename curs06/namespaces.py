var = 1
msg = 'Hello 1'
def functie():
    msg = 'Hello'
    global var #nu e recomandat sa fie folosit
    print(var, 'linia 4')
    var = 2
    print(var, 'linia 4')
    return msg
print(var, 'linia 6')
functie()
print(var, 'linia 9')
print(msg)