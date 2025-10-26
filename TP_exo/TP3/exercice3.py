def car(bool):
    if bool == True:
        return 'T'
    else:
        return 'F'
    
def formule(a,b):
     return not (a and b)
    
def formule_3(a, b, c):
    return (a or not c) and (not a or b) and (not b or c)

def table_2_verite(ft):
    L = [True, False]
    print('a', 'b', 'P')
    for i in range(len(L)):
        for j in range(len(L)):
            print(car(L[i]), car(L[j]), car(ft(L[i], L[j])))

def ft_1(a, b):
    return not (a and b)

def ft_2(a, b):
    return not a or not b

def ft_3(a, b):
    return not (a or b)
def ft_4(a, b):
    return not a and not b
            
def table_3_verite(ft):
    L = [True, False]
    print('a', 'b', 'c', 'P')
    for i in range(len(L)):
        for j in range(len(L)):
            for g in range(len(L)):
                print(car(L[i]), car(L[j]), car(L[g]), car(ft(L[i], L[j], L[g])))

def egalite_formules_2(f1, f2):
    L = [True, False]
    for i in range(len(L)):
        for j in range(len(L)):
                if f1(L[i], L[j]) != f2(L[i], L[j]):
                    return False
    return True 
    