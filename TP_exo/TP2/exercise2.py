def suivant(u):
    if u % 2 == 0:
        return u // 2
    else:
        return 3 * u + 1
    
def suracuse(u):
    print(u, '-->', end=' ')
    while u != 1:
        print(suivant(u), end=' ')
        u = suivant(u)       
        if u != 1:
            print('-->', end=' ')
            
def nombre_syracuse(u):
    flag = 0
    while u != 1:
        u = suivant(u)
        flag = flag + 1
    print(flag+1)    
    
    
assert suivant(5) == 16
assert suivant(16) == 8
assert suivant(12) == 6
assert suivant(8) == 4