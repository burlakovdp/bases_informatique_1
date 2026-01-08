import tkinter as tk
from math import *

cx = 0
cy = 0
couleur = 'black'

root = tk.Tk()
root.title("TD 4")

Largeur=500
Hauteur=500

Dessin = tk.Canvas(root, height=Hauteur, width=Largeur, bg='white')

def deplacer(x, y):
    global cx
    cx = x
    global cy
    cy = y
    
def changer_couleur(c):
    global couleur
    couleur = c
    
def tracer(x, y):
    Dessin.create_line(cx, cy, x, y, fill=couleur)
    deplacer(x, y)

def dessine_maison(x, y, c):
    global cx
    global cy
    deplacer(x, y)
    tracer(cx + c, cy)
    tracer(cx, cy-c)
    tracer(cx - c, cy)
    tracer(cx, cy+c)
    deplacer(cx, cy-c)
    changer_couleur('red')
    tracer(cx+c//2, cy - sqrt(c**2-(c//2)**2))
    tracer(cx+c//2, cy + sqrt(c**2-(c//2)**2))

def distance(p,q):
    return sqrt((q[0]-p[0])**2+(q[1]-p[1])**2)

def affiche_pixel(x, y, couleur):
    Dessin.create_rectangle(x, y, x, y, fill=couleur, outline='')
    
def disque(x0, y0, r, couleur):
    for j in range(Hauteur):
        for k in range(Largeur):
            if (distance((k,j),(x0, y0)) < r):
                affiche_pixel(k, j, couleur)

def cercle_X(x, y, r, couleur):
    for j in range(Hauteur):
        for k in range(Largeur):
            if (r-0.5 <= distance((k,j),(x, y)) <= r+0.5):
                affiche_pixel(k, j, couleur)
    
class Cercle:
    
    def __init__(self, x, y, couleur, rayon):
        self.cord = (x,y)
        self.couleur = couleur
        self.rayon = rayon
    
    def afficher_disque(self):
        disque(self.cord[0], self.cord[1], self.rayon, self.couleur)
    
    def afficher_cercle(self):
        cercle_X(self.cord[0], self.cord[1], self.rayon, self.couleur)
        

def couleur_rgb(r,g,b):

    res = ''
    if r == 0:
        res += '00'
    if g == 0:
        res += '00'
    if b == 0:
        res += '00'
        
    tmp = 0
    calors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    while  b > 0:
      tmp = b % 16
      res = calors[tmp] + res
      b = b // 16
    while  g > 0:
      tmp = g % 16
      res = calors[tmp] + res
      g = g // 16
    while  r > 0:
      tmp = r % 16
      res = calors[tmp] + res
      r = r // 16
    
    res = '#' + res
    return res









test_disque = Cercle(100, 100, 'red', 50)
test_disque.afficher_disque()

test_cercle = Cercle(300, 300, 'red', 50)
test_cercle.afficher_cercle()

#distace((10, 10), (50, 50))

#dessine_maison(100, 500, 200)

Dessin.pack()
root.mainloop()