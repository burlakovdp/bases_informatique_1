def ex1a():
    for i in range(1, 8):
        print(i, end='')
        if i != 7:
            print(', ', end='')
def ex1b():
    for i in range(1, 14, 2):
        print(i, end='')
        if i != 13:
            print(', ', end='')
        
def ex1c():
    for i in range(17, -2, -3):
        print(i, end='')
        if i != -1:
            print(', ', end='')

def ex1g():
    for i in range(7):
        print(i+1)
        
def nombre_apparition(c, s):
    counter = 0
    for i in range(len(s)):
        if c == s[i]:
            counter += 1
    return counter

def absence_de_e(s):
    return nombre_apparition('e', s) == 0 and nombre_apparition('E', s) == 0
        
def affiche_miroir(s):
    '''
    print(s, end=' ')
    for i in range(len(s)-1, -1, -1):
        print(s[i], end='')
    '''
    print(s, miroir(s))
        
def affiche_miroir2(s):
    print(s, end=' ')
    counter = len(s)-1
    for i in range(len(s)):
        print(s[i+counter], end='')
        counter -= 2
        
def miroir(s):
    res = ''
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    return res

def est_un_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def nombre_presents(liste_resultats):
    res = 0
    for i in range(len(liste_resultats)):
        if liste_resultats[i] != 'ABS':
            res += 1
    return res

def moyenne(liste_resultats):
    res = 0
    for i in range(len(liste_resultats)):
        if liste_resultats[i] != 'ABS':
            res += liste_resultats[i]
    return res // len(liste_resultats)

def bilan(liste_resultats):
    res = []
    counter = 0
    for i in range(len(liste_resultats)):
        if liste_resultats[i] != 'ABS':
            if int(liste_resultats[i]) > 9:
                counter += 1
    res += str(counter)
    return res

def entrelacement(s1,s2):
    res = ''
    for i in range(len(s1)):
        res += s1[i]
        res += s2[i]
    return res
        
def bien_ponctuée(s):
    for i in range(len(s)):
        if i < len(s)-1:
            if s[i] == '.' and s[i + 1] != ' ':
                return False
    return True
           
def est_pangramme(line):
    check = [0]*26
    line = line.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(line)):
        for j in range(len(alphabet)):
            if line[i] == alphabet[j]:
                check[j] += 1
    for k in range(len(check)):
        if check[k] == 0:
            return False
    return True
    
            
                

                 
            
    


        
