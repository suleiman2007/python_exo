from tkinter import *

def cesar():
    text = str(input_text.get())
    cle = int(input_cle.get())
    output_text = ""
    for i in text:
        output_text += chr(ord(i) + cle)
    result_place.set(output_text)


fenetre = Tk()
fenetre.title("")

Label(fenetre, text='Le text à chiffrer :').grid(row=0, column=0)
input_text = Entry(fenetre)
input_text.grid(row=0, column=1)
Label(fenetre, text='La clé :').grid(row=1, column=0)
input_cle = Entry(fenetre)
input_cle.grid(row=1, column=1)

Label(fenetre, text='Le resultat :').grid(row=2, column=0)
result_place = StringVar()
Label(fenetre, textvariable=result_place).grid(row=2, column=1)

BoutonCalculer=Button(fenetre,text='Calculer', command = cesar).grid(row=6,column=1,pady=10)
Button(fenetre,text='Quitter', command = fenetre.quit).grid(row=6,column=2,pady=10)

fenetre.mainloop()
fenetre.destroy()
