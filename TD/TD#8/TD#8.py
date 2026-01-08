import random

CHEMIN = '/Users/burlakov/Desktop/Univ/TD#8/dictionnaire.txt'
MY_CHEMIN = '/Users/burlakov/Desktop/Univ/TD#8/ex1.txt'

def ensemble_de_lettres(chemin):
    fichier = open(chemin, 'r', encoding='utf-8')
    res = {x for ligne in fichier for x in ligne if x.isalpha()}
    fichier.close()
    return res

def statistique_lettre(chemin):
    fichier = open(chemin, 'r', encoding='utf-8')
    res = {}
    lettres = ensemble_de_lettres(chemin)
    for lettre in lettres:
        res[lettre] = 0
    for ligne in fichier:
        for lettre in ligne:
                if lettre in res:
                    res[lettre] += 1
    fichier.close()
    return res

def bilan(chemin, chemin_bilan):
    fichier = open(chemin_bilan, 'w', encoding='utf-8')

    statistique = statistique_lettre(chemin)
    first_lettre = None
    second_lettre = None

    for lettre in statistique:
        if first_lettre is None:
            first_lettre = lettre
        elif statistique[lettre] > statistique[first_lettre]:
            first_lettre = lettre
    nom = chemin.split('/')
    nom = nom[-1]
    fichier.write(f'La lettre la plus présente dans le fichier {nom} est {first_lettre}\n')
    statistique[first_lettre] = 0

    for lettre in statistique:
        if second_lettre is None:
            second_lettre = lettre
        elif statistique[lettre] > statistique[second_lettre]:
            second_lettre = lettre
    fichier.write(f'La lettre la plus présente dans le fichier {nom} est {second_lettre}\n')    
    fichier.close()

def extraire_dictionnaire():
    fichier = open(CHEMIN, 'r', encoding='utf-8')
    dico = [mot[:-1] for mot in fichier]
    return dico        

def longueur_max(dict):
    counter = -1
    for e in dict:
        if e > counter:
            counter = e
    return counter
#print(ensemble_de_lettres(MY_CHEMIN))
#print(statistique_lettre(MY_CHEMIN))
#bilan(CHEMIN, MY_CHEMIN)
"""
dico = extraire_dictionnaire()
L = []
for i in range(len(dico)):
    if dico[i].isalpha():
        L.append(len(dico[i]))
        print(f'{i} {dico[i]} {len(dico[i])}')
print(longueur_max(L))
print(max(L))

for mot in dico:
    if len(mot) == longueur_max(L):
        print(mot)
#print(L[:3])
"""
DICO = extraire_dictionnaire()

def str_to_list(mot):
    res = [e for e in mot]
    return res

def mot_au_hasard():
    return DICO[random.randint(0, len(DICO)-1)]

def cache_lettre(mot):
    res = ['_']*len(mot)
    res[0], res[-1] = mot[0], mot[-1]
    return ''.join(res)

def ajoute_lettre(mot, secret, lettre):
    res = ""
    for i in range(len(mot)):
            if secret[i] == lettre:
                res += lettre
            else:
                res += mot[i]
    return res


def pluriel(nombre, mot):
    if nombre > 1:
        mot = mot+ "s"
        return (f'{nombre} {mot}') 
    return (f'{nombre} {mot}') 
"""
assert pluriel(3,"chat") == "3 chats"
assert ajoute_lettre('abcd', cache_lettre('abcd'), 'b') == "ab_d"
assert ajoute_lettre('abcd', cache_lettre('abcd'), 'a') == "a__d"
assert ajoute_lettre('abcd', cache_lettre('abcd'), 'c') == "a_cd"
assert ajoute_lettre('abcd', cache_lettre('abcd'), 'd') == "a__d"
assert ajoute_lettre('abcd', cache_lettre('abcd'), 'g') == "a__d"
assert ajoute_lettre('abcd', cache_lettre('abcd'), 'm') == "a__d"
assert ajoute_lettre('abcd', cache_lettre('abcd'), '3') == "a__d"
assert ajoute_lettre('abcd', cache_lettre('abcd'), 'l') == "a__d"
"""

#for i in range(10):
#   print(cache_lettre(mot_au_hasard()))
def nouvelle_partie(vies) :
    secret = mot_au_hasard() # le mot a deviner
    mot = cache_lettre(secret) # le mot partiellement decouvert
    print('il te reste' , vies , 'vies', " chut :", secret)
    while vies > 0 and '_' in mot :
        print(mot)
        c = input('Quelle lettre demandes-tu, humain ? ')
        ancien_mot=mot
        mot=ajoute_lettre(mot,secret,c)
        if mot != ancien_mot :
            print('Bien joué !')
        else :
            vies = vies-1
            print('Raté… Il te reste ' + pluriel(vies,'vie')+'.' )
        print(f'vies -> {vies}, mot -> {mot}')
    if vies == 0 :
        print('PENDU! Le mot secret était' , secret + '. On rejoue ?')
    else :
        print(mot)
        print('GAGNÉ ! On rejoue ?')
#print(ajoute_lettre('abcd', cache_lettre('abcd'), 'h'))
#print((pluriel(3,"chien") , pluriel(1,"chat")))
nouvelle_partie(10)

