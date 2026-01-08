def code_cesar_lettre(c,k):
    if ord(c) < 65 or ord(c) > 90:
        return c
    num = ord(c)+k
    if num > 90:
        return chr((num%90)+64)
    else:
        return chr(num)
        
def code_cesar(msg,k):
    res = ''
    for i in range(len(msg)):
        res += code_cesar_lettre(msg[i], k)
    return res

def decoder_cesar_lettre(c, k):
    if ord(c) < 65 or ord(c) > 90:
        return c   
    num = ord(c)-k
    if num < 65:
        return chr(90-(64%num))
    else:
        return chr(num)
    
def decoder_cesar(msg):
    res = ''
    for i in range(1, 26):
        for j in range(len(msg)):
            res += decoder_cesar_lettre(msg[j], i)
        print(res)
        res = ''