def suite0():
    for i in range(0, 11):
        print(i/10, end='')
        if i/10 != 1.0:
            print('-->', end='')

def suite1():
    for i in range(0, 201, 5):
        print(i/10, end='')
        if i/10 != 20.0:
            print('-->', end='')

def suite2():
    for i in range(10, -11, -2):
        print(i, end='')
        if i != -10:
            print(' --> ', end='')
            
def suite3():
    counter = 1
    for i in range(0, 100):  
        if i < 10:
            print(0, i, sep='', end =' ')
        else:
            print(i, end=' ')
        if counter % 10 == 0:
            print('')
        counter += 1
        
def somme(list1):
    res = 0
    for i in range(len(list1)):
        res += list1[i]
    return res

def combien_de_e(line):
    res = 0
    for i in range(len(line)):
        if line[i] == 'e':
            res += 1
    return res

def maximum(list1):
    res = 0
    for i in range(len(list1)):
        if res < list1[i]:
            res = list1[i]
    return res

def plus_longue(list1):
    res = ''
    for i in range(len(list1)):
        if len(res) < len(list1[i]):
            res = list1[i]
    return res

def replacer_e_par_euro(line):
    res = ''
    for i in range(len(line)):
        if line[i] == 'e':
            res += '€'
        else:
            res += line[i]
    return res

def valeur_absolue_tuple(tuple1):
    res = ()
    for i in range(len(tuple1)):
        res = res + (abs(tuple1[i]), )
    return res

def position(num, list1):
    for i in range(len(list1)):
        if num == list1[i]:
            return i
    return -1

def appartient(num, list1):
    for i in range(len(list1)):
        if num == list1[i]:
            return True
    return False

def appartient(lettre, line):
    for i in range(len(line)):
        if lettre == line[i]:
            return True
    return False

def tiret(line):
    res = ''
    for i in range(len(line)):
        res += line[i]
        if i < len(line)-1:
            res += '-'
    return res
            