#Ex 2
'print(ord('r'))'
'''
for i in range(0, 10):
    print(ord(str(i)))
'''

def liste_chiffres():
    res = ''
    for i in range(ord('0'), ord('9')+1):
        res += chr(i)
        
    for j in range(ord('A'), ord('Z')+1):
        res += chr(j)
    return res
    
def ecrire_nombre(n, b):
    if n == 0:
        return '0'
    chaine = liste_chiffres()
    res = ''
    while n > 0:
        res = chaine[n % b] + res
        n = n // b
    return res
    
def valeur(ch):
    chaine = liste_chiffres()
    for i in range(len(chaine)):
        if ch == chaine[i]:
            return i
    return None

def lire_nombre(chaine, b):
    res = 0
    for i in range(len(chaine)):
        res = res * b + valeur(chaine[i])
    return res
    
#Ex.3

def couleur_rgb(r, g, b):
    res = '#'
    res += ecrire_nombre(r, 16) + ecrire_nombre(g, 16) + ecrire_nombre(b, 16)
    return res
    
#Ex. 4

def decoder(chaine):
    res = [0]*len(chaine)  
    for i in range(len(chaine)):
        res[i] = ord(chaine[i])
    return res

def est_ascii(ch):
    for i in range(len(ch)):
        if ord(ch[i]) < 0 or ord(ch[i]) > 127:
            return False
    return True

def recoder(L):
    res = ''
    for i in range(len(L)):
        if est_ascii(chr(L[i])) == True:
            res += chr(L[i])
        else:
            res += '?'
    return res

#Ex.5
def check_lower(lettre):
    if ord(lettre) >= ord('a') and ord(lettre) <= ord('z'):
        return True
    else:
        return False

def check_upper(lettre):
    if ord(lettre) >= ord('A') and ord(lettre) <= ord('Z'):
        return True
    else:
        return False

def HURLER(line):
    res = ''
    for i in range(len(line)):
        if check_lower(line[i]):
            res += chr(ord(line[i]) - 32)
        else:
            res += line[i]
    print(res)
    
def murmurer(line):
    res = ''
    for i in range(len(line)):
        if check_upper(line[i]):
            res += chr(ord(line[i]) + 32)
        else:
            res += line[i]
    print(res)

def ft_upper(lettre):
    if check_lower(lettre):
        return chr(ord(lettre) - 32)
    else:
        return lettre
    
def ft_alpha_check(char):
    if (ord(char) >= ord('A') and ord(char) <= ord('Z')) or (ord(char) >= ord('a') and ord(char) <= ord('z')):
        return True
    else:
        return False
    
def title(chaine):
    res = ''
    flag = False
    for i in range(len(chaine)):
        if i == 0 and check_lower(chaine[i]):
            res += ft_upper(chaine[i])
        elif not(ft_alpha_check(chaine[i])):
            res += chaine[i]
            flag = True       
        elif flag == True:
            res += ft_upper(chaine[i])
            flag = False
        else:
            res += chaine[i]
    return res

def ft_chiffre(chiffre):
    if ord(str(chiffre)) >= ord('0') and ord(str(chiffre)) <= ord('9'):
        return True
    else:
        return False
    
def chaine_vers_liste(ch):
    res = [0]*len(ch)
    res_counter = 0
    mem = ''
    
    for i in range(len(ch)):
        if ft_chiffre(ch[i]):
            mem += ch[i]
        elif ch[i] == ',':
            res[res_counter] = mem
            res_counter += 1
            mem = ''
            
    res[res_counter] = mem
    res1 =[0]*(res_counter+1)
    for i in range(res_counter+1):
        res1[i] = res[i]
    return res1


def anton():
    line = 'anton'
    mem = ''
    for i in range(4, -1, -1):
        print(f'len(line) = {len(line)-1}')
        print(f'i = {i}')
        mem += line[i]
        print(f'mem = {mem}')
    print(mem)