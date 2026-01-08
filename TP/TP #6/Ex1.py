def apparaît_old(x,L):
    for e in L:
        if e == x:
            return True
    return False

def apparaît(x,L):
    return x in L

def contient(L1,L2):
    for e in L1:
        if not apparaît(e, L2):
            return False
    return True

def commun(L1,L2):
    for e in L1:
        if apparaît(e, L2):
            return e
    return False
test = []
test1 = [1, 2, 3]
test2 = [1, 2]
test3 = [1, 2, 3]
test4 = [1, 2, 3, 4]

assert(apparaît(1, test1)) == True
assert(apparaît(0, test1)) == False
assert(apparaît('', test)) == False

assert(contient(test1, test2)) == False
assert(contient(test3, test4)) == True
assert(contient(test4, test3)) == False

assert(commun(test4, test3)) == True
assert(commun(test1, test4)) == True
assert(commun(test, test1)) == False