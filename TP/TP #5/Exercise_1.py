import tkinter as tk
# On crée une fenêtre
root = tk.Tk()
root.title("Arc-en-ciel")
# On crée un canvas (zone de dessin)
Hauteur = 500
Largeur = 500
Dessin=tk.Canvas(root,height=Hauteur,width=Largeur,bg="white")
Dessin.pack()

def cercle(x,y,rayon,épaisseur,couleur):
    p = (x-rayon,y-rayon)
    q = (x+rayon,y+rayon)
    Dessin.create_oval(p,q,width=épaisseur,outline=couleur)
def disque(x,y,rayon,couleur):
    p = (x-rayon,y-rayon)
    q = (x+rayon,y+rayon)
    Dessin.create_oval(p,q,width=0,fill=couleur)

epp = 50
Dessin.create_rectangle(0, 0, 550, 250, fill='#7799FF', outline='#7799FF')

cerc_r = 200 
colors = ['purple', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red'] 

for color in colors:
    cercle(250,250,cerc_r, epp, color)
    cerc_r -= 20

disque(250,250,85,'#7799FF')
Dessin.create_rectangle(0, 550, 550, 250, fill='green', outline='green')
root.mainloop()