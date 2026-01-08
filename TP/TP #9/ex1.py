import tkinter as tk
from math import *
(Hauteur,Largeur) = (300,300)
root = tk.Tk()
root.title("Exprimons nos émotions")
Dessin = tk.Canvas(root,height=Hauteur,width=Largeur,bg='white')
Dessin.pack()

def disque(x,y,r,couleur):
    p = (x+r,y+r)
    q = (x-r,y-r)
    Dessin.create_oval(p,q,fill=couleur)

class Etat():
    def __init__(self):
        self.yeux=20
        self.heureux = False
        self.affichage()
    def affichage(self):
        Dessin.delete('all')
        # Tête
        (xt,yt)=(Largeur/2,Hauteur/2)
        Rt=Hauteur*.9/2
        disque(xt,yt,Rt,'yellow')
        # Œil à droite de l’image
        (xd,yd)=(2*Largeur/3,Hauteur/3)
        disque(xd,yd,self.yeux,'black')
        # Œil à gauche de l’image
        (xg,yg)=(Largeur/3,Hauteur/3)
        disque(xg,yg,self.yeux,'black')
        # Bouche
        (xe,ye)=(Largeur/2,2*Hauteur/3)
        (Rex,Rey)= (40,30)
        Dessin.create_oval(xe-Rex,ye-Rey,xe+Rex,ye+Rey,fill='yellow',width=5)
        if self.heureux == True:
            (xr,yr)=(Largeur/2,2*Hauteur/3-20)
        else:
            (xr,yr)=(Largeur/2,2*Hauteur/3+20)
        (Rrx,Rry)=(70,20)
        Dessin.create_rectangle(xr-Rrx,yr-Rry,xr+Rrx,yr+Rry,fill='yellow',width=0)
etat=Etat()

def heureux():
    etat.heureux = True
    etat.affichage()
def malheureux():
    etat.heureux = False
    etat.affichage()

def change_taille(x):
    etat.yeux = int(x)/2
    etat.affichage()

bouton1 = tk.Button(root,text="Content",command=heureux,width=9)
bouton2 = tk.Button(root,text="Pas content",command=malheureux,width=9)
curseur = tk.Scale(root, orient="horizontal", length=Largeur,
label='Rayon',command=change_taille,
from_=1, to=100)
bouton1.pack()
bouton2.pack()
curseur.pack()



root.mainloop()