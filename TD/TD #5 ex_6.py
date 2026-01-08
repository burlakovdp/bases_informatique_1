import tkinter as tk
from math import *

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

cx = 0
cy = 0
couleur = 'black'

root = tk.Tk()
root.title("TD 4")

Largeur=1000
Hauteur=500

Dessin = tk.Canvas(root, height=Hauteur, width=Largeur, bg='pink')

def gris(i):
    res = couleur_rgb(255 - (255 * i//49), 255 - (255 * i//49), 255 - (255 * i//49))
    return res

disque_x = 100
disque_y = 100


for col in range(5):
    est_disque = Cercle(disque_x, disque_y, 'red', 50)
    for lin in range(5):
        test_disque = Cercle(disque_x, disque_y, 'red', 50)
        test_disque.afficher_disque()
        disque_x += 200
    disque_y -= 100

Dessin.pack()
root.mainloop()