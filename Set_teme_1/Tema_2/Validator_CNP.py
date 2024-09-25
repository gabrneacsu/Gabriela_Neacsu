cnp = input('Introduceti CNP-ul de verificat: ')
cod_validare_c = '279146358279'
rezultat = 'Felicitari, CNP introdus cu succes!'
aa = ll = zz = jj = nnn = c = 0
is_bisect = True
if not cnp.isdigit() or len(cnp) != 13:
    rezultat = 'Format CNP invalid!'
elif cnp.isdigit() and len(cnp) == 13:
    if int(cnp[0]) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        rezultat = 'Prima cifra a CNP-ului nu indica sexul corect!'
    elif int(cnp[0]) in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        for i in range(0, 12):
            c += int(cnp[i]) * int(cod_validare_c[i])
        if c % 11 == 10:
            c = 1
        else:
            c = c % 11
        if c != int(cnp[12]):
            rezultat = 'Codul C din CNP este invalid!'
        #calculez anul in care este nascuta persoana
        if int(cnp[0]) in [1, 2, 7, 8, 9]:
            aa = 1900 + int(cnp[1]) * 10 + int(cnp[2])
        elif int(cnp[0]) in [3, 4]:
            aa = 1800 + int(cnp[1]) * 10 + int(cnp[2])
        elif int(cnp[0]) in [5, 6]:
            aa = 2000 + int(cnp[1]) * 10 + int(cnp[2])
        #de vazut daca anul e bisect
        if (aa % 4 == 0 and aa % 100 != 0) or (aa % 400 == 0):
            is_bisect = True
        elif aa % 4 != 0:
            is_bisect = False
        ll = int(cnp[3]) * 10 + int(cnp[4]) #valoarea lunii de nastere
        zz = int(cnp[5]) * 10 + int(cnp[6]) #valoarea zilei de nastere
        jj = int(cnp[7]) * 10 + int(cnp[8])
        nnn = int(cnp[9]) * 100 + int(cnp[10]) * 10 + int(cnp[11])
        #verific daca luna nasterii este valida
        if ll not in range(1, 13):
            rezultat = 'Luna din CNP este invalida!'
        elif ll in [1, 3, 5, 7, 8, 10, 12]:
            if zz not in range(1, 32):
                rezultat = 'Ziua din CNP este invalida!'
        elif ll in [4, 6, 9, 11]:
            if zz not in range(1, 31):
                rezultat = 'Ziua din CNP este invalida!'
        elif ll == 2:
            if (is_bisect and zz not in range(1, 30)) or (not is_bisect and zz not in range(1, 29)):
                rezultat = 'Ziua din CNP este invalida!'
        if jj not in range(1, 47) or jj != 51 or jj != 52:
            rezultat = 'Codul judetului din CNP este invalid!'
        if nnn not in range(1, 1000):
            rezultat = 'Codul NNN din CNP este invalid!'

print(rezultat)

#idee: de facut un dictionar cu toate lunile, judetele etc (ex: 01 ian) pentru o afisare mai buna