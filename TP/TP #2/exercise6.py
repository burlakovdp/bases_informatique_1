def etoile():
    print('*',end='')

def diese() :
    print('#',end='')

def nouvelle_ligne() :
    print()

def barre_1():
    print('/',end='')

def barre_2():
    print('\\',end='') # Il faut échapper le symbole de backslash
    
def tapis_c(l,h):
    for i in range(h):
        nouvelle_ligne()
        for j in range(l):
            if i == 0 or i == h-1:
                etoile()
            else:
                if j == 0 or j == l-1:
                    etoile()
                else:
                    diese()

def tapis_b(l,h):
    for i in range(h):
        nouvelle_ligne()
        for j in range(l):
            if j == h-i-1:
                etoile()
            else:
                diese()
                
def tapis_c(l,h):
    point = 0
    point2 = l - 2
    for i in range(h):
        nouvelle_ligne()
        if i > 0:
            point = point + 2
        if i > h//2:
            point2 = point2 - 2
        for j in range(l):
            if i < h // 2: 
                flag = ((l-2)-point)//2
                if j < flag:
                    diese()
                if j == flag:
                    barre_1()
                if j > flag and j < flag + 1 + point and j <= point + flag:
                    diese()
                if j == flag + point:
                    barre_2()
                if j > flag + 1 + point:
                    diese()
            else:
                flag = ((l-2)-point2)//2
                #print('point', point2)
                #print(flag)
                if j < flag:
                    diese()
                if j == flag:
                    barre_2()
                if j > flag and j < flag + 1 + point2 and j <= point2 + flag:
                    diese()
                if j == flag + point2:
                    barre_1()
                if j > flag + 1 + point2:
                    diese()
            
def ligne(l_e, step, flag):
    if flag == 0:
        line = l_e*'#' + '/' + step*'#' + '\\' + l_e*'#'
    else:
        line = l_e*'#' + '\\' + step*'#' + '/' + l_e*'#'
    return line 

def tapis_c1(l, h):
    i = 0
    j = 0
    step = 0
    flag = 0
    while i < h:
        if i < h//2:
            start = (l - 2 - step)//2
            print(ligne(start, step, flag))
            #print(f'start ={start}, point={step}, fin={start}')
            i += 1
            step += 2
        else:
            step -= 2
            flag = 1
            start = (l - 2 - step)//2
            #print(f'start ={start}, point={step}, fin={start}')
            print(ligne(start, step, flag))
            i += 1
            

            
        
    
    