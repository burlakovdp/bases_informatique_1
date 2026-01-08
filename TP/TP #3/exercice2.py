def concatenation(L1,L2):
    res = [0] * (len(L1) + len(L2))
    for i in range(len(L1)):
        res[i] = L1[i]   
    for i in range(len(L1), len(L1) + len(L2)):
        res[i] = L2[i-len(L1)]
    return res 

assert concatenation(['a','b','c'], ['g','f','h']) == ['a','b','c','g','f','h']
assert concatenation([],[]) == []
assert concatenation(['a','b','t'], ['g','f','h','p','l']) == ['a','b','t','g','f','h','p','l']
assert concatenation(['a'], ['g','f','h']) == ['a','g','f','h']
assert concatenation(['a','b','c','t','z','!'], ['g','f','h','4','a','m','v']) == ['a','b','c','t','z','!','g','f','h','4','a','m','v']
assert concatenation([], ['g','f','h']) == ['g','f','h']
assert concatenation(['g','f','h'], []) == ['g','f','h']
