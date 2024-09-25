"""Sa da de la tastatura un string. Sa se elimine caracterele din string pornind de la 0 pana la n,
unde n e dat si el de la tastatura"""

s = input('introduceti un string: ')
n = input('introduceti un numar: ')
if n.isdigit() and (n := int(n)) and n<=len(s): # a doua conditie = realocare
        s = s[n:]
        print(s)

# recomandare: evita if in if pe cat posibil