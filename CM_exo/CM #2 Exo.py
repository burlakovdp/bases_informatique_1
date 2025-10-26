#Écrire une fonction table_multiplication(n) qui affiche la table de n.
def table_multiplication(n):
    i = 0
    while i < n:
        print(i, '*', n, '=', i*n)
        i += 1
#Pour un entier n>1, on cherche le plus petit d>1 tel que d divise n.
def plus_petit_facteur(n):
    d = 2
    while d <= n:
        if n % d == 0:
            return d
        else:
            d += 1
            
def ft_suite(n):
    u0 = 234
    i = 0
    while i < n:
        u0 = u0*(-8/10) + 3
        i += 1
    return u0

def u(n):
    if n == 0:
        return 234
    else:
        return -8/10 * u(n-1)+3
    return u