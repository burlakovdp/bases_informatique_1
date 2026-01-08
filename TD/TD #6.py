#Ex. 1
test = [1, 2, 3, 4, 'ABS']
test1 = [1, 2, 'ABS', 4, 'ABS']
def modifier_ABS(liste):
    for i in range(len(liste)):
        if liste[i] == 'ABS':
            test[i] = 0

def ABS_vers_zero_basique(liste):
    res = [0] * len(liste)
    for i in range(len(liste)):
        if liste[i] == 'ABS':
            res[i] = 0
        else:
            res[i] = liste[i]
    return res

def ABS_vers_zero(liste):
    res = []
    for i in range(len(liste)):
        if liste[i] == 'ABS':
            res.append(0)
        else:
            res.append(liste[i])
    return res

def filtre_notes(liste):
    res = [x for x in liste if x != 'ABS']
    return res

ABS_vers_zero_basique(test)
assert(test == [1, 2, 3, 4, 'ABS'])

modifier_ABS(test)

assert(test == [1, 2, 3, 4, 0])

#Ex.2

def ex2(num):
    if num == 1:
        res = []
        for i in range(4):
            res.append(i*i)
        return res
    elif num == 2:
        res = []
        for i in range(11):
            res.append((i, 10-i))
        return res
    elif num == 3:
        res = []
        for i in range(11):
            if i % 2 == 0:
                res.append(i)
        return res 

#Ex.3

def max_pair(liste):
    tmp = None
    for e in liste:
        if (e % 2 == 0 and (tmp == None or tmp < e)):
            tmp = e 
    if tmp == None:
        raise ValueError('Pas de valeur paire')
    return tmp


def afficher_max_pair(liste):
    try:
        print('Le plus grand pair est', max_pair(liste))
    except ValueError:
        print('De la musique avant toute chose,\nEt pour cela préfère l’Impair,\nPlus vague et plus soluble dans l’air,\nSans rien en lui qui pèse ou qui pose.')
        pass

        



test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
test4 = [-1, 3, 1]

#Ex.4

def est_triee(L):
    tmp = L[0]
    for i in range(1, len(L)):
        if tmp < L[i]:
            tmp = L[i]
            continue
        else:
            return False
    return True

test5 = [1, 5, 4]
assert(est_triee(test5)) == False

#Ex.5

def grouper(L):
    res = []
    for e in L:
        if res == [] or e != res[-1]:
            res.append(e)
    return res

def compacter(L):
    if L == []:
        return []
    res = []
    counter = 0
    tmp = None
    for i in range(len(L)):
        if tmp == None:
            tmp = L[i]
        elif L[i] != tmp:
            counter += 1
            res.append((counter, tmp))
            counter = 0
            tmp = L[i]
        else:
            counter += 1
    res.append((counter+1, tmp))
    return res
test56 = [4, 4, 4, 2, 3]

print(compacter(test56))
print(grouper(test56))