def etoile():
    print('*',end='')

def diese() :
    print('#',end='')

def nouvelle_ligne() :
    print()
    
def tapis_a(l,h):
    for i in range(h):
        nouvelle_ligne()
        for j in range(l):
          etoile()

def tapis_b(l,h):
    for i in range(h):
        nouvelle_ligne()
        for j in range(l):
            if j % 2 == 0:
                etoile()
            else:
                diese()
                
def tapis_c(l, h):
    flag = 1
    for i in range(h):
        nouvelle_ligne()
        if i % 2 == 0:
            flag = 1
        else:
            flag = 0
        for j in range(l):
            if j % 2 == 0 and flag == 1:
                etoile()
            elif flag == 1:
                diese()
            elif j % 2 != 0 and flag == 0:
                etoile()
            else:
                diese()
def tapis_d(l, h):
    flag = 1
    counter = 0
    for i in range(h):
        counter = counter + 1
        nouvelle_ligne()
        if i % 2 == 0:
            flag = 1
        else:
            flag = 0
        for j in range(l):
            if counter % 3 == 0:
                etoile()
            elif j % 2 == 0 and flag == 1:
                etoile()
            elif flag == 1:
                diese()
            elif j % 2 != 0 and flag == 0:
                etoile()
            elif flag == 0:
                diese()
                
            