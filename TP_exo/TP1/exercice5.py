import random as r

def choix_ordi():
    return r.randint(1, 100)
i = 7
number = choix_ordi()
while i != 0:
    choix_h = input('Ton choix, humain : ')
    
    if int(choix_h) > number:
        print('-')
        i = i - 1 
    elif int(choix_h) < number:
        print('+')
        i = i - 1
    elif int(choix_h) == number:
        print('Tu as gagné, Humain !')
        i = 0