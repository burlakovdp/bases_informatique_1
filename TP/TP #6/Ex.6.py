import tkinter as tk
import random
L = [10,5,5,10,7,10,10,5,11,11,11]
def ft_count(e, L):
    counter = 0
    for el in L:
        if e == el:
            counter += 1
    return counter
def effectif(L):
    return [(i, ft_count(i, L)) for i in range(min(L), max(L)+1)]
def height_searcher(max_column, our_column, max_height_column):
    return (our_column * max_height_column)//max_column
def max_sizer_sercher(line):
    tmp = []
    for i in range(len(line)):
        tmp.append(line[i][1])
    return max(tmp)
def etap(n):
    sum = 0
    for _ in range(n):
        sum += random.randint(0,1)
    return sum

# On crée une fenêtre
root = tk.Tk()
root.title("Jeu de go")
# On crée un canvas (zone de dessin)
Hauteur = 800
Largeur = 800
global_couleur = 'black'
Dessin=tk.Canvas(root,height=Hauteur,width=Largeur,bg="white")
Dessin.pack()
hasard = [etap(i) for i in range(200)]
print(hasard)
cord = effectif(hasard)
print(cord)
size_indent = 10 #recul
size_line = Largeur-(2*size_indent) #taille de ligne
size_column = size_line // len(cord)  #largeur de colonne
max_height_column = Hauteur - 2*size_indent #hauteur de colonne(max)
start_pointX = size_indent
max_size_of_column = max_sizer_sercher(cord)



Dessin.create_line(size_indent, Hauteur-size_indent, Largeur-size_indent, Hauteur-size_indent, fill='black')
for i in range(len(cord)):
    if height_searcher(max_size_of_column, cord[i][1], max_height_column) == 0:
        start_pointX += size_column
    else:
       #Dessin.create_rectangle(start_point, size_indent+height_searcher(cord[-1][1], cord[i][1], max_height_column), start_point+size_column, Hauteur-(size_indent+height_searcher(cord[-1][1], cord[i][1], max_height_column)), fill='black')
        Dessin.create_rectangle(start_pointX, Hauteur-size_indent, start_pointX+size_column, Hauteur-size_indent-height_searcher(max_size_of_column, cord[i][1], max_height_column), fill='dodgerblue4', outline='black')
        start_pointX += size_column



root.mainloop()