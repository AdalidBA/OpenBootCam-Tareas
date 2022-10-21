from select import select
import tkinter
from tkinter import ttk

defatultext="Seleccione una opción"

window=tkinter.Tk()
opcion=tkinter.StringVar()

window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)
window.columnconfigure(4,weight=2)

label=ttk.Label(text=defatultext)
label.grid(column=0,row=0)

label=ttk.Label(text=defatultext)
label.grid(column=0,row=0)

# v1=ttk.IntVar()
# v2=ttk.IntVar()
# v3=ttk.IntVar()
r1=tkinter.Checkbutton(text="Opcion 1" )
r2=tkinter.Checkbutton(text="Opcion 2")
r3=tkinter.Checkbutton(text="Opcion 3")

r1.grid(column=0,row=1)
r2.grid(column=0,row=2)
r3.grid(column=0,row=3)

btn=ttk.Label(text="Mi texto ")
btn.grid(column=0,row=4)


window.mainloop()