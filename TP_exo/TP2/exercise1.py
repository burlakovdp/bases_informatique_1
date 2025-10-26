def fac_rec(n):
    if n == 0:
        return 1
    else:
        return n*fac_rec(n-1)

def fac(n):
    res = 1
    while n != 0:
        res = res*n
        n = n - 1
    return res