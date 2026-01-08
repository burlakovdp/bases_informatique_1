import tkinter as tk
# On crée une fenêtre
root = tk.Tk()
root.title("Jeu de go")
# On crée un canvas (zone de dessin)
Hauteur = 704
Largeur = 704
global_couleur = 'black'
Dessin=tk.Canvas(root,height=Hauteur,width=Largeur,bg="white")
Dessin.pack()

def cercle(x,y,rayon,épaisseur,couleur):
    p = (x-rayon,y-rayon)
    q = (x+rayon,y+rayon)
    Dessin.create_oval(p,q,width=épaisseur,outline=couleur)

def disque(x,y,rayon,couleur):
    p = (x-rayon,y-rayon)
    q = (x+rayon,y+rayon)
    Dessin.create_oval(p,q,width=1,fill=couleur, outline='black')

def cord_transformerX(x0):
    if x0 > 19 or x0 < 1:
        return -1 
    res_x = delta*2 + (x0-1)*delta 
    return res_x

def cord_transformerY(y0):
    if y0 > 19 or y0 < 1:
        return -1
    res_y = (Hauteur-delta*2) - (y0-1)*delta 
    return res_y

def place_pierre(x,y,couleur):
    disque(cord_transformerX(x), cord_transformerY(y), delta//2, couleur)

def place_pierre_2(x,y):
    global global_couleur
    disque(cord_transformerX(x), cord_transformerY(y), delta//2, global_couleur)
    if global_couleur == 'black':
        global_couleur = 'white'
    else:
        global_couleur = 'black'

delta = Hauteur/22
Dessin.create_rectangle(delta, delta, Largeur-delta, Hauteur-delta, fill='#C8A165',outline='black')

cord = delta*2
for _ in range(19): #vertical lines
    Dessin.create_line(cord, delta*2, cord, Hauteur-delta*2, fill='black')
    cord+=delta

cord = delta*2
for _ in range(19): #vertical lines
    Dessin.create_line(delta*2, cord, Largeur-delta*2, cord, fill='black')
    cord+=delta

for i in range(4,17, 6): #9 first noir pierres
    for j in range(4, 17, 6):
        disque(cord_transformerX(i),cord_transformerY(j), delta//4, 'black')
'''
place_pierre(17,16,'black')
place_pierre(4,16,'white')
place_pierre(16,3,'black')
place_pierre(4,4,'white')
place_pierre(6,17,'black')
'''
place_pierre_2(17,16)
place_pierre_2(4,16)
place_pierre_2(16,3)
place_pierre_2(4,4)
place_pierre_2(6,17)

root.mainloop()