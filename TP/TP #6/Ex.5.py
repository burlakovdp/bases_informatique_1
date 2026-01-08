import random
LIST_DE_PONCTUATION = [",", "'", ".", ":", ";", "!", "?", " "]

def liste_vers_chaîne(L):
    res = ''
    for e in L:
        res += e
    return res

def melange(m):
    if m in LIST_DE_PONCTUATION or len(m) == 1:
        return m
    res = ''
    res += m[0]
    mem = m[1:-1]
    mem = list(mem)
    random.shuffle(mem)
    tmp = liste_vers_chaîne(mem)
    res += tmp
    res += m[-1]
    return res

def liste_des_mots(m):
    word = ''
    res = []
    for e in m:
        if e not in LIST_DE_PONCTUATION:
            word += e
        else:
            if word != "":
                res.append(word)
            res.append(e)
            word = ''
    return res

def melange_texte(s):
    res = ''
    line = liste_des_mots(s)
    for e in line:
        res += liste_vers_chaîne(melange(e))
    return res


print(melange_texte("Les hommes naissent et demeurent libres et égaux en droits. Les distinctions sociales ne peuvent être fondées que sur l'utilité commune."))

