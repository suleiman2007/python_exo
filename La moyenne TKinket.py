from tkinter import *

fenetre = Tk()
fenetre.title('Calcule moyenne')

Label(fenetre, text="Nombre 1", borderwidth=20).grid(row=0, column=0)
Label(fenetre, text="Nombre 2", borderwidth=20).grid(row=0, column=1)
Label(fenetre, text="Nombre 3", borderwidth=20).grid(row=0, column=2)

var_nom1 = Entry(fenetre)
var_nom1.grid(row=1, column=0)
var_nom1.insert(0,"0")
var_nom2 = Entry(fenetre)
var_nom2.grid(row=1, column=1)
var_nom2.insert(0,"0")
var_nom3 = Entry(fenetre)
var_nom3.grid(row=1, column=2)
var_nom3.insert(0,"0")

Label(fenetre, text="Coef 1 ", borderwidth=20).grid(row=2, column=0)
Label(fenetre, text="Coef 2", borderwidth=20).grid(row=2, column=1)
Label(fenetre, text="Coef 3", borderwidth=20).grid(row=2, column=2)

var_coef1 = Entry(fenetre)
var_coef1.grid(row=3, column=0)
var_coef1.insert(0,"0")
var_coef2 = Entry(fenetre)
var_coef2.grid(row=3, column=1)
var_coef2.insert(0,"0")
var_coef3 = Entry(fenetre)
var_coef3.grid(row=3, column=2)
var_coef3.insert(0,"0")

Label(fenetre, text="Moyenne", borderwidth=20).grid(row=4, column=0)
moyenne = StringVar()
Label(fenetre, textvariable=moyenne, borderwidth=20).grid(row=4, column=1)

def calculer():
    sum_element = sum([float(var_nom1.get()), float(var_nom2.get()), float(var_nom3.get())])
    sum_coef = sum([float(var_coef1.get()),float(var_coef2.get()),float(var_coef3.get())])
    moyenne.set(sum_element / sum_coef)

BoutonCalculer=Button(fenetre,text='Calculer', command = calculer).grid(row=6,column=1,pady=10)
Button(fenetre,text='Quitter', command = fenetre.quit).grid(row=6,column=2,pady=10)

fenetre.mainloop()
fenetre.destroy()