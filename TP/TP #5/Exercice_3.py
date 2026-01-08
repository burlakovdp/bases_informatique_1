import tkinter as tk
# On crée une fenêtre
root = tk.Tk()
root.title("Tracer des droites")
# On crée un canvas (zone de dessin)
Hauteur = 500
Largeur = 500
Dessin=tk.Canvas(root,height=Hauteur,width=Largeur,bg="white")
Dessin.pack()

def affiche_pixel(x,y,couleur):
    Dessin.create_rectangle(x,y,x,y,fill=couleur,outline='')

def entier_le_plus_proche(q):
    return round(q)

def affiche_segment(p1,p2):

    if p2[0] < p1[0]:
        p1, p2 = p2, p1

    a = (p2[1]-p1[1])/(p2[0]-p1[0])
    b = p1[1] - a*p1[0]

    if abs(p1[1] - p2[1]) > abs(p2[0]-p1[0]):
        for i in range(p1[1], p2[1]+1):
            x = (i-b)/a
            affiche_pixel(entier_le_plus_proche(x), i, 'red')
    else:
        for i in range(p1[0], p2[0]+1):
            y = a*i + b
            affiche_pixel(i, entier_le_plus_proche(y), 'blue')
            

p1= (100, 200)
p2= (200, 500)
affiche_segment(p1, p2)

x0 = 100
y0 = 100
start_point = 100
end_point = 300
for i in range(201):
    for j in range(201):
        if x0 == end_point or x0 == start_point or y0 == end_point or y0 == start_point:
            affiche_pixel(x0, y0, 'red')
        x0 += 1
    x0 = 100
    y0 += 1
root.mainloop()