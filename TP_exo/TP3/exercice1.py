alphabet="abcdefghijklmnopqrstuvwxyz"
assert len(alphabet) == 26

def indice(lettre):
    for i in range(len(alphabet)):
        if lettre == alphabet[i]:
            return i
    return 26

def statistiques(texte):
    res = [0]*27  
    for j in range(len(texte)):
        j = indice(texte[j])
        res[j] += 1
    return res

def affichage(tableau):
    for i in range(len(tableau)):
        if i > 25:
            print('Autres :', tableau[i])
        else:
            if tableau[i] != 0:
                print(alphabet[i], ':', tableau[i])
                
def plus_frequent(tableau):
    maximum = 0
    imax=0
    for i in range(len(tableau)-1):
        if maximum < tableau[i]:
            maximum = tableau[i]
            imax=i
    return alphabet[imax]
        
def plus_fréquent_bis(tableau):
    maximum = 0
    for i in range(len(tableau)-1):
        if maximum < tableau[i]:
            maximum = tableau[i]
    for i in range(len(tableau)-1, -1, -1):
        if maximum == tableau[i]:
            return alphabet[i]
        
def tous_les_plus_fréquents(tableau):
    res = ''
    maximum = 0
    for i in range(len(tableau)-1):
        if maximum < tableau[i]:
            maximum = tableau[i]
    for i in range(len(tableau)):
        if maximum == tableau[i]:
            res += alphabet[i]
    return res
    
    