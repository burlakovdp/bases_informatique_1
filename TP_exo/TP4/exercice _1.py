print(ord('A'))
print(ord('D'))
print(ord('0'))
print(ord('3'))

for i in range(ord('A'), ord('Z')+1):
    print(chr(i), end= ' ')

print()
for i in range(ord('a'), ord('z')+1):
    print(chr(i), end= ' ')
    
print()    
for i in range(ord('0'), ord('9')+1):
    print(chr(i), end= ' ')
    
def ft_alphabet(lettre):
    alphabet = ''
    for i in range(ord('A'), ord('Z')+1):
        alphabet += chr(i)
    for j in range(len(alphabet)):
        if alphabet[j] == lettre:
            return j
        
def est_chiffre(c):
    if ord(c) > ord('9') or ord(c) < ord('0'):
        return False
    else:
        return True

def masquer_numero(s):
    res = ''
    for i in range(len(s)):
        if est_chiffre(s[i]) == True:
            res += '*'
        else:
            res += s[i]       
    return res
                




assert est_chiffre('(') == False
assert est_chiffre('=') == False
assert est_chiffre('0') == True
assert est_chiffre('9') == True

