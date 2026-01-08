import tkinter as tk
from math import *
(Hauteur,Largeur) = (500,500)
root = tk.Tk()
root.title("Balon")
Dessin = tk.Canvas(root,height=Hauteur,width=Largeur,bg='white')
Dessin.pack()

class Etat():
    def __init__(self):
        self.x = 200
        self.y = 200
        self.r = 50
        self.affichage()
        self.temps = 0
        self.sens = True
        self.pas = 1
        self.pause = False

    def ballon(self,x,y,r):
        p=(x-r,y-r) ; p1=(x-2.5*r,y-r) ; p2=(x+2.5*r,y-r)
        q=(x+r,y+r) ; q1=(x-.5*r, y+r) ; q2=x+.5*r, y+r
        Dessin.create_oval(p,q,fill='orange',outline='black',width=5)
        Dessin.create_line((x,y-r),(x,y+r),width=5)
        Dessin.create_arc(p1,q1, extent=80, start=-40, width=5,style='arc')
        Dessin.create_arc(p2,q2, extent=80, start=140, width=5,style='arc')

    def affichage(self):
        Dessin.delete('all')
        self.ballon(self.x, self.y, self.r)
etat = Etat()
def tictac():
    etat.temps = etat.temps+1
    etat.affichage()
    if etat.pause == False:
        anim() 
    Dessin.after(5,tictac)

def anim():
    if etat.y + etat.r > Hauteur:
        etat.sens = False
    if etat.y - etat.r == 0:
        etat.sens = True
    if etat.sens == False:
        etat.y -= etat.pas
    else:
        etat.y += etat.pas

def stop(event):
    if etat.pause == True:
        etat.pause = False
    else:
        etat.pause =  True

root.bind('<space>', stop)
tictac()
root.mainloop()