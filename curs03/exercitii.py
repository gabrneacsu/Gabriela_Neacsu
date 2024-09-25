nr_tel = input("tel: ")

valid = True
if len(nr_tel) == 12 and nr_tel[0:3] == '+40':
    for i in nr_tel[3:13]:
        if i not in '1234567890':
            valid = False
            break
else:
    valid = False

if not valid:
    print('invalid')
else:
    print('valid')
