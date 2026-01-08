choix_h = input('Ton choix, humain : ')

choix_pc = 50
i = 7
tmp = 12

while i != 0:
    print("J'ai choisi : ", choix_pc)
    
    if choix_pc == choix_h:
        print("J'ai gagné")
        i = 0
        break
    
    choix_signe = input('Humain : ')
    
    if choix_signe == '+':
        if i == 7:
            choix_pc = choix_pc + 25
        else:
            choix_pc += tmp
    elif choix_signe == '-':
        if i == 7:
            choix_pc = choix_pc - 25
        else:
            choix_pc -= tmp
       
    if choix_pc == int(choix_h):
        print("J'ai gagne, ton chiffre c'est : ", choix_pc)
        i = 0
        break
    
    i = i - 1
    if tmp != 1 and i != 6:
        tmp = tmp // 2
    
        
        