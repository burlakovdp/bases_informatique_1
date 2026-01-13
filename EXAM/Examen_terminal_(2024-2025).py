"""
Exercise 1
"""
def entier(ch):
    print(ord(ch) - ord('0'))

def chiffre(n):
    if n >= 0 and n <= 9:
        print(chr(n + ord('0')))

def tester_identifiant(ch):
    for number in ch:
        try:
            entier(number)
        except:
            return False
    return True

def ajouter_clé(ch):
    chiffre = 0
    for i in range(len(ch)):
        if i % 2 == 0:
            chiffre += (int(ch[i]) * 3)
        else:
            chiffre += (int(ch[i]) * 1)
    if len(str(chiffre)) != 0:
        cle = 10 - int(len(str(chiffre)))
    else:
        cle = 0
    ch += str(cle)
    return ch

entier('2')
chiffre(8)
"""
Exercise 2
"""
valeurs = "3211-2221-2122-1411-1132-1231-1114-1312-1213-3112"
def chaînes_vers_liste(ch):
    res = []
    tmp = ''
    for char in ch:
        if char == '-':
            res.append(tmp)
            tmp = ''
        else:
            tmp += char
    res.append(tmp)
    return res


def traduire_vers_chaîne(ch, format):
    res = ''
    if format == "A":
        for i in range(len(ch)):
            if i % 2 == 0:
                for num in range(int(ch[i])):
                    res += '0'
            else:
                for num in range(int(ch[i])):
                    res += '1'
    else:
        for i in range(len(ch)):
            if i % 2 == 0:
                for num in range(int(ch[i])):
                    res += '1'
            else:
                for num in range(int(ch[i])):
                    res += '0'  
    return res

print(traduire_vers_chaîne('9633', "A"))
print(traduire_vers_chaîne('3693', "C"))

def encoder(ch):
    res = ''
    res += '101'
    for num in ch[0:4]:
        if num == '9':
            res += traduire_vers_chaîne('3112', "A")
        elif num == '6':
            res += traduire_vers_chaîne('1114', "A")
        elif num == '3':
            res += traduire_vers_chaîne('1411', "A")
    res += '01010'
    for num in ch[4:8]:
        if num == '9':
            res += traduire_vers_chaîne('3112', "C")
        elif num == '6':
            res += traduire_vers_chaîne('1114', "C")
        elif num == '3':
            res += traduire_vers_chaîne('1411', "C")
    res += '101'
    return res

assert(encoder("96333693")) == '1010001011010111101111010111101010101000010101000011101001000010101'

"""
Exercise 3
"""
import tkinter as tk
# Variables globales
Hauteur = 500
Largeur = 700
Marge = 100
# On crée une fenêtre et un canevas (zone de dessin)
root = tk.Tk()
root.title("Générateur de code barre")
Dessin=tk.Canvas(root,height=Hauteur,width=Largeur,bg="white")
Dessin.pack()

def calculer_delta(n):
    return ((Largeur - Marge*2)//n)

def tracer_colonne(n, d):
    for i in range(n):
        Dessin.create_rectangle(Marge + Marge*i,Marge,(Marge + Marge*i)+d,Hauteur-Marge,fill="black")

def tracer_code_barre(numéro):
    for i in int(encoder(numéro)):
        pass


def formater_chaîne(ch):
    res = ''
    if len(ch) < 12:
        for i in range(len(ch)):
            res += ch[i]
        for i in range(12 - len(ch)):
            res += ' '
    elif len(ch) > 12:
        for i in range(12):
            res += ch[i]
    else:
        return ch
    return res








print(formater_chaîne("CHAUSSETTE sdfijsoijfiojsdfi"))