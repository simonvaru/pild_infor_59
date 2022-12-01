from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()

##############CONSTRUCCION BARRA DE MENU##################################

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_command(label="Salir")

borrarMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
borrarMenu.add_command(label="Borrar campos")

crudMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerac de...")

###########################################################################
#################COMIENZO DE CAMPOS VACIOS X RELLENAR######################

miFrame=Frame(root)
miFrame.pack()

cuadroID=Entry(miFrame)
cuadroID.grid(row=0, column=1,padx=10,pady=10)

cuadroNOMBRE=Entry(miFrame)
cuadroNOMBRE.grid(row=1, column=1,padx=10,pady=10)
cuadroNOMBRE.config(fg="black", justify="right")

cuadroPASS=Entry(miFrame)
cuadroPASS.grid(row=2, column=1,padx=10,pady=10)
cuadroPASS.config(show="*")

cuadroAPELLIDO=Entry(miFrame)
cuadroAPELLIDO.grid(row=3, column=1,padx=10,pady=10)

cuadroDIRECCION=Entry(miFrame)
cuadroDIRECCION.grid(row=4, column=1,padx=10,pady=10)

textoCOMENTARIO=Text(miFrame, width=16, height=5)
textoCOMENTARIO.grid(row=5, column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame, command=textoCOMENTARIO.yview)
scrollVert.grid(row=5, column=2,sticky="nsew")
textoCOMENTARIO.config(yscrollcommand=scrollVert.set)





###########################################################################
root.mainloop()
