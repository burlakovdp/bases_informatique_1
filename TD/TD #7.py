#import nsinfo
#Ex.1

PileErreur=ValueError('Pile vide')

my_list = [1, 2, '-', 3, 4, '+', '*']
list3 = [2, 5, '+', 3, '*', 7, '/']
LIST_SIGNE = ['-', '+', '*', '/']
def pile_calculator(list):
    MY_PILE = nsinfo.Pile()
    for e in list:
        if e in LIST_SIGNE:
            signe = e
            b = MY_PILE.depiler()
            a = dépile(MY_PILE)
            if signe == '-':
                res = a - b
            if signe == '+':
                res = a + b
            if signe == '*':
                res = a * b
            if signe == '/':
                res = a / b
            empile(MY_PILE, res)
        else:
            empile(MY_PILE, e)
    return dépile(MY_PILE)
    
    

def nouvelle_pile():
    return []

def empile(L,e):
    L.append(e)

def dépile(L):
    if L == []: raise PileErreur
    return L.pop()

def sommet(L):
    if L == []: raise PileErreur
    return L[len(L)-1]

def est_vide(L):
    return L == []

#print(pile_calculator(list3))

#Ex.2

M_test = [[2, 4, 6], [8, 10, 12]]
M_test2 = [[1, 2, 3], [4, 5, 6]]

def dimension(M):
    return (len(M), len(M[0]))

def matrice_nulle(n ,m):
    res = []
    for ligne in range(n):
        res.append([])
        for e in range(m):
            res[ligne].append(0)
    return res

def doubler(M):
    (n, m) = dimension(M)
    for ligne in range(n):
        for e in range(m):
            M[ligne][e] *= 2

def double(M):
    (n, m) = dimension(M)
    res = matrice_nulle(n, m)
    for ligne in range(n):
        for e in range(m):
            res[ligne][e] = M[ligne][e] * 2
    return res

def est_le_double(M1, M2):
    if dimension(M1) != dimension(M2):
        return -1
    (n, m) = dimension(M1)
    for ligne in range(n):
        for e in range(m):
            if M1[ligne][e] * 2 != M2[ligne][e]:
                return False
    return True
''''
print(dimension(M_test))
(n, m) = dimension(M_test)
print(matrice_nulle(n, m))
print(M_test)
#doubler(M_test)
print(double(M_test))
'''
print(est_le_double(M_test2, M_test))

#Ex.3

TAILLE_PILE = -1
DEBUT_PILE = -2
CAPACITE_PILE = -3


def indice_haut_pile(pile):
    DEBUT = DEBUT_PILE
    TAILLE = TAILLE_PILE
    return pile[DEBUT] + pile[TAILLE]

def initialiser(taille_tableau, capacité):  
    res = [0 for i in range(taille_tableau+3)]
    res[taille_tableau] = capacité
    return res

def est_vide(pile):
    return pile[TAILLE_PILE] == 0

def est_pleine(pile):
    return pile[TAILLE_PILE] == pile[CAPACITE_PILE]

def push(pile, x):
    pile[indice_haut_pile] = x
    pile[TAILLE_PILE] += 1

def pop(pile):
    res = pile[indice_haut_pile-1]
    pile[indice_haut_pile-1] = 0
    pile[TAILLE_PILE] -= 1
    return res

res = initialiser(10, 4)
print(res)
#def est_vide(pile)