import pnm
import matrice

#pnm.voir_fichier('space-invader-pieuvre.pbm' , quadrillage=False)
#voir_fichier('space-invader-soucoupe.pbm', quadrillage=False)

M = pnm.fichier_vers_matrice('space-invader-pieuvre.pbm')
#print(M)

def affiche_matrice_booléens(M,plein,vide):
    (ligne, colonnes) = matrice.dimensions(M)
    for i in range(ligne):
        for j in range(colonnes):
            if M[i][j] == False:
                print(vide, end='')
            else:
                print(plein, end='')
        print()
        print()

#affiche_matrice_booléens(M,'#','.')
def ajout_ligne(ligne1, ligne2):
    res = [0] * (len(ligne1) + len(ligne2))
    for i in range(len(ligne1)):
        res[i] = ligne1[i]
    for j in range(len(ligne2)):
        res[len(ligne1)+j] = ligne2[j]
    return res

def ajoute_horizontal(M1,M2):
    (ligne1, colonnes1) = matrice.dimensions(M1)
    (ligne2, colonnes2) = matrice.dimensions(M2)

    matrice_res = matrice.nouvelle_matrice(ligne1, colonnes1+colonnes2)

    for i in range(ligne1):
            matrice_res[i] = ajout_ligne(M1[i], M2[i])
    return matrice_res

def ajoute_vertical(M1,M2):
    flag = True
    (ligne1, colonnes1) = matrice.dimensions(M1)
    (ligne2, colonnes2) = matrice.dimensions(M2)
    nl = ligne1 + ligne2
    nc = max(colonnes1, colonnes2)
    
    res = matrice.nouvelle_matrice(nl, nc)
       
    for i in range(ligne1):
        for j in range(colonnes1):
                res[i][j] = M1[i][j]

    for i in range(ligne2):
        for k in range(colonnes2):
                res[i+ligne1][k] = M2[i][k]
    return res

'''
M = pnm.fichier_vers_matrice('space-invader-pieuvre.pbm')
M2 = ajoute_horizontal(M , M)
M3 = ajoute_horizontal(M2 , M)
pnm.matrice_vers_fichier(M3 , 'space-invader-3-pieuvres.pbm')
pnm.voir_fichier('space-invader-3-pieuvres.pbm')

M = pnm.fichier_vers_matrice('space-invader-pieuvre.pbm')
'''
def répète_horizontal(M,k):
    res = M
    for i in range(k-1):
        res = ajoute_horizontal(res, M)
    return res


def create_army(M1, M2, nS, nE):
    army1 = répète_horizontal(M1, nS)
    army2 = répète_horizontal(M2, nS)
    army1 = ajoute_vertical(army1, army2)
    for i in range(nE//2):
        army1 = ajoute_vertical(army1, army1) 
    return army1
        
         
'''
M1 = répète_horizontal(M, 20)
affiche_matrice_booléens(répète_horizontal(M,20),"#",".")

pnm.matrice_vers_fichier(M1 , 'space-invader-20-pieuvres.pbm')
'''
'''
M = pnm.fichier_vers_matrice('space-invader-pieuvre.pbm')
M1 = pnm.fichier_vers_matrice('space-invader-pieuvre.pbm')
M2 = ajoute_vertical(M , M1)
M3 = ajoute_vertical(M2 , M)
M4 = ajoute_vertical(M3 , M)
pnm.matrice_vers_fichier(M4 , 'space-invader-TEST-pieuvres.pbm')
pnm.voir_fichier('space-invader-TEST-pieuvres.pbm')
affiche_matrice_booléens(M4, '#', '.')
'''

pieuvre = pnm.fichier_vers_matrice('space-invader-pieuvre.pbm')
soucoupe = pnm.fichier_vers_matrice('space-invader-soucoupe.pbm')
army = create_army(pieuvre, soucoupe,20, 10)
pnm.matrice_vers_fichier(army , 'space-invader-ARMY-pieuvres.pbm')
pnm.voir_fichier('space-invader-ARMY-pieuvres.pbm')
