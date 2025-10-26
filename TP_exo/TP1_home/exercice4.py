import random as r

def choix_ordi():
    choix = r.randint(1, 3)
    if choix == 1:
        choix_pc = 'pierre'
    elif choix == 2:
        choix_pc = 'feuille'
    else:
        choix_pc = 'ciseaux'
    return choix_pc

def logic(msg, choix_pc):
    if msg == choix_pc:
        return 'Egalite'
    if msg == 'pierre' and choix_pc == 'feuille':
        return 'ordinateur'
    elif msg == 'feuille' and choix_pc == 'pierre':
        return 'humain'
    elif msg == 'pierre' and choix_pc == 'ciseaux':
        return 'humain'
    elif msg == 'ciseaux' and choix_pc == 'pierre':
        return 'ordinateur'
    elif msg == 'feuille' and choix_pc == 'ciseaux':
        return 'ordinateur'
    elif msg == 'ciseaux' and choix_pc == 'feuille':
        return 'humain'
    
choix_pc = choix_ordi()
print('Quel est ton choix, humain?')
msg = input()

if msg == 'pierre' or msg == 'feuille' or msg == 'ciseaux':
    print('Ok')
else:
    msg = choix_ordi()
    print('Choix incorrect, je vais choisir pour toi :', msg)
    
print('Humain : ', msg)
print('Ordinateur : ', choix_pc)
print('Vainqueur : ', logic(msg, choix_pc))