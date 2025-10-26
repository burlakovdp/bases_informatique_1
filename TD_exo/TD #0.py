def est_pair(n):
    return n % 2 == 0

def bissextile(annee):
    return annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)

def anne_normale(annee):
    return annee % 4 > 0 or (annee % 100 == 0 and annee % 400 > 0)

def bonjour(prenom, nom):
    rep = 'Bonjour ' + prenom + ' ' + nom + ' !'
    return rep

def repetition(mot, n):
    return (mot + ', ') * (n-1) + mot

def est_majeur(j0, m0, a0, j1, m1, a1):
    return a1 - a0 > 18 or ((a1-a0 == 18 and m1-m0 > 0) or (a1-a0 == 18 and m1-m0 == 0 and j1 -j0 >= 0))
