import random

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def fact_while(n):
    res = 1
    while n != 0:
        res = res * n
        n = n - 1
    return res

def u(n):
    if n == 0:
        return 234
    else:
        return (-2/3)*u(n-1) + 1/2
    
def suite(n):
    res = 234
    while n != 0:
        res = (-2/3)*res + 1/2
        n = n - 1
    return res

def tester(n):
    i = 0
    flag = True
    while i <= n:
        if suite(i) != u(i):
            flag = False
        else:
            i = i + 1
    return flag

def racine_entier(n):
    k = 1
    while k**2 <= n:
        k = k + 1
    return k - 1

def noter():
    res = random.randint(0, 20)
    flag = random.randint(1, 3)
    if flag == 1 and res != 20:
        res = res + 0.5
    elif flag == 2 and res != 0:
        res = res - 0.5
    return res

def noter_gentil(n):
    res = noter()
    while n != 0:
        tmp = noter()
        if tmp >= res:
            res = tmp
        n = n - 1
    return res

def moyenne(k, n):
    somme = 0
    tmp = k
    while k != 0:
        somme += noter_gentil(n)      
        k = k - 1
    return somme / tmp
        
def etoile():
    print('*', end='')

def diese():
    print('#', end='')

def nouvelle_ligne():
    print()
    
def frise(n):
    i = 0
    while i < n:
        if i % 2 != 0:
            etoile()
        else:
            diese()
        i += 1
    return nouvelle_ligne()

def affiche_calcul_binaire(n):
    while n > 0:
        print(n % 2, 'car',n, '=', '2 x', n//2, '+', n % 2)
        n = n // 2 

def affiche_binaire(n):
    res = ''
    while n > 0:
        res = str(n % 2) + res
        n = n // 2
    print(res)
        