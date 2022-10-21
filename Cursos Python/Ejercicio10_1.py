from select import select
import tkinter
from tkinter import ttk

defatultext="Seleccione una opción"

window=tkinter.Tk()
opcion=tkinter.StringVar()

def seleccion():
    label.config(text="Ha seleccionado la opcion {}".format(opcion.get()))
    
def reset():
    label.config(text=defatultext)
    opcion.set(None)

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=2)

label=ttk.Label(text=defatultext)
label.grid(column=0,row=0)

r1=ttk.Radiobutton(text="Opcion 1", value=1, variable=opcion, command=seleccion)
r2=ttk.Radiobutton(text="Opcion 2", value=2,variable=opcion, command=seleccion)
r3=ttk.Radiobutton(text="Opcion 3", value=3,variable=opcion, command=seleccion)

r1.grid(column=0,row=1)
r2.grid(column=0,row=2)
r3.grid(column=0,row=3)

btn=ttk.Button(text="Reiniciar",command=reset)
btn.grid(column=0,row=4)


window.mainloop()