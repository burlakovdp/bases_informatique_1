import random as r

def choix_ordi():
    choix = r.randint(1, 3)
    if choix == 1:
        return 'pierre'
    elif choix == 2:
        return 'feuille'
    else:
        return 'ciseaux'
 
def logic(msg, pc):
    if msg == pc:
        return 'Egalite'
    if msg == 'pierre' and pc == 'feuille':
        return 'Ordinateur'
    elif msg == 'feuille' and pc == 'pierre':
        return 'Humain'
    elif msg == 'pierre' and pc == 'ciseaux':
        return 'Humain'
    elif msg == 'ciseaux' and pc == 'pierre':
        return 'Ordinateur'
    elif msg == 'feuille' and pc == 'ciseaux':
        return 'Ordinateur'
    elif msg == 'ciseaux' and pc == 'feuille':
        return 'Humain'
    


choix_pc = choix_ordi()
print('Quel est ton choix humain ?')
msg = input()
print('Humain tu as choisi', msg)

if msg == 'pierre' or msg == 'feuille' or msg == 'ciseaux':
    print('Ok')
else:
    msg = choix_ordi()
    print('Choix incorrect, je vais choisir pour toi...', msg)
    
print('Huimain :', msg)
print('Ordinateur :', choix_pc)
print('Vainqueur :', logic(msg, choix_pc))
    