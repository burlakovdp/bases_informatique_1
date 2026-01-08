import tkinter as tk
# On crée une fenêtre
root = tk.Tk()
root.title("Mon emploi du temps")
# On crée un canvas (zone de dessin)
Hauteur = 700
Largeur = 1100
Dessin=tk.Canvas(root,height=Hauteur,width=Largeur,bg="white")
Dessin.pack()

delta_h = 50
delta_l = 100

root.mainloop()