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
        
     
    


    
    
        