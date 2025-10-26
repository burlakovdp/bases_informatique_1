def max(a, b):
    if a > b:
        return a
    else:
        return b

def max4(a, b, c, d):
    return max(max(a, b), max(c, d))

def max4_sans_max(a, b, c, d):
    if a > b:
        tmp1 = a
    else:
        tmp1 = b
    if c > d:
        tmp2 = c
    else:
        tmp2 = d
    if tmp1 > tmp2:
        return tmp1
    else:
        return tmp2
    
def meme_signe(a, b):
    if (a >= 0 and b >= 0) or (a < 0 and b < 0):
        return True
    else:
        return False
    
def f_abs(x):
    if x < 0:
        return x * -1
    else:
        return x
    
def max_abs(x, y):
    if f_abs(x) > f_abs(y):
        return x
    if f_abs(x) == f_abs(y):
        return max(x, y)
    if f_abs(x) < f_abs(y):
        return y
    
def afficher_max_abs(x, y, msg):
    if f_abs(x) > f_abs(y):
        print(msg,x)
    if f_abs(x) == f_abs(y):
        print(msg, max(x, y))
    if f_abs(x) < f_abs(y):
        print(msg, y)

def hms(n):
    h = n // 3600
    m = (n - (h * 3600)) // 60
    s = n - (h * 3600 + m * 60)
    text_h = 'heure'
    text_m = 'minute'
    text_s = 'seconde'
    if h > 1:
        text_h = text_h + 's'
    if m > 1:
        text_m = text_m + 's'
    if s > 1:
        text_s = text_s + 's'
    print(n, '--->', h, text_h, m, text_m, s, text_s)
    
    
assert max(1, 2) == 2
assert max(2, 3) == 3
assert max(5, 4) == 5
assert max4(1, 2, 3, 4) == 4
assert max4(1, 2, 5, 7) == 7
assert max4(0, -1, 10, 5) == 10
assert max4_sans_max(1, 2, 3, 4) == 4
assert max4_sans_max(1, 2, 5, 7) == 7
assert max4_sans_max(0, -1, 10, 5) == 10
assert meme_signe(-1, 0) == False
assert meme_signe(2, 3) == True
assert meme_signe(-1, -2) == True
assert meme_signe(-1, 5) == False
assert meme_signe(0, 0) == True
assert meme_signe(4.0, 0) == True
assert meme_signe(5, 1)
assert max_abs(2, -3) == -3
assert max_abs(-3, -1) == -3
assert max_abs(3, 0) == 3