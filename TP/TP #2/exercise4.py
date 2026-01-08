def fermat(n):
    return 2**(2**n) + 1

def premier_facteur(n):
    i = 2
    while True:
        if n % i == 0:
            return i
        i = i + 1

def fermat_checker():
    n=0
    while premier_facteur(fermat(n)) == fermat(n):
        print('premier n - >', fermat(n))
        print('premier_facteur - >', premier_facteur(fermat(n)))
        n = n + 1