"""
Exercice 1 — L’ensemble des lettres minuscules
"""
minuscules = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

def nb_occurrences_minuscules(chaîne):
    counter = 0
    for lettre in chaîne:
        if lettre in minuscules:
            counter += 1
    return counter 
assert(nb_occurrences_minuscules('AaAaBz')) == 3

def ensemble_minuscules(chaîne):
    res = set()
    for lettre in chaîne:
        if lettre in minuscules:
            res.add(lettre)
    return res

assert(ensemble_minuscules('AaAaBz')) == {'a','z'}

def nb_minuscules(chaîne):
    return len(ensemble_minuscules(chaîne))

assert(nb_minuscules('AaAaBz')) == 2


"""
Exercice 2 — Le temps qui passe
"""
def jour(chemin):
    fichier = open(chemin, mode='w', encoding='utf-8')

    for h in range(24):
        for m in range(0, 60, 5):
            fichier.write(f'{h:0>2}:{m:0>2}\n')

    fichier.close()
#jour("TD/test.txt")


"""
Exercice 3 — Liste de contacts
"""
contacts = {'Chloé': '0601020304', 'Quentin': '0710203040', 'Lyes': '0623344556'}

#contacts['Chloé'] = '0611223344'
#contacts['Sarah'] = '0145444342'
#contacts.pop('Chloé')

def affichage_détail(contacts):
    for name in contacts:
        print(f'{name} : {contacts[name]}')

#affichage_détail(contacts)

"""
Exercice 4 — Liste de contacts inversée
"""
def inverse_liste_contacts(contacts):
    res = dict()
    for name in contacts:
        res[contacts[name]] = name
    return res

#print(inverse_liste_contacts(contacts))

L = [ ('10:03', '0710203040'), ('9:45', '0710203040'), ('hier','0800123123'), ('20/11', '0601020304')]

def affiche_liste_appels(L ,contacts):
    contacts_inverse = inverse_liste_contacts(contacts)
    for couple in L:
        if couple[1] in contacts_inverse:
            print(f'{couple[0]} {contacts_inverse[couple[1]]}')
        else:
            print(f'{couple[0]} {couple[1]}')
        
#affiche_liste_appels(L ,contacts)
"""
Exercice 5 — Export et import
"""

def sauvegarde(contacts, chemin) :
    fichier = open(chemin, mode="w", encoding="utf-8")

    for name in contacts:
        fichier.write(f'{name},{contacts[name]}\n')

    fichier.close()

#sauvegarde(contacts, "TD/contacts.txt")

def découper(chaîne):
    res = chaîne[:len(chaîne)-1].split(',')
    return res

def importer(chemin):
    res = dict()
    fichier = open(chemin, mode="r", encoding="utf-8")
    
    for ligne in fichier:
        tmp = découper(ligne)
        res[tmp[0]] = tmp[1]    
    fichier.close()

    return res 
#print(importer("TD/contacts.txt"))
"""
Exercice 6 — Liste de contacts inversée avec répétitions
"""
contacts2 = {'Maison Chloé': '0901020304', 'Maison Lyes': '0901020304', 'Alex': '0412345678'}

def inverse_liste_contacts2(contacts):

    res = dict()
    numbers = []
    for name in contacts:
        if contacts[name] not in numbers:
            numbers.append(contacts[name])

    for number in numbers:
        tmp = []
        for name in contacts:
            if contacts[name] == number:
                tmp.append(name)
        res[number] = tmp
    
    return res

print(inverse_liste_contacts2(contacts2))