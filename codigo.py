from tkinter import *
from tkinter import messagebox
import sqlite3
from funciones import *



###########################FUNCIONES######################################
def conexionBBDD():
    miConexion=sqlite3.connect('pild_infor_59/Usuarios')
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATAUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100)) 
            ''')
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except:
        messagebox.showwarning("¡Atencion!", "La BBDD ya existe")

        
def salir_app():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()
        
def limpiar_campos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    textoCOMENTARIO.delete(1.0, END)

def crear():
    miConexion=sqlite3.connect("pild_infor_59/Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("INSERT INTO DATAUSUARIOS VALUES(NULL,'" + miNombre.get()+"','" + miApellido.get()+"','" + miPass.get()+"','" + miDireccion.get()+"','" + textoCOMENTARIO.get("1.0", END)+"')")
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro insertado con exito")

        
def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATAUSUARIOS WHERE ID=" + miId.get())
    elUsuario=miCursor.fetchall()
    for usuario in elUsuario:
        miId.set(usuario[0]) 
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miPass.set(usuario[3])
        miDireccion.set(usuario[4])
        textoCOMENTARIO.insert(1.0, usuario[5])   
        
    miConexion.commit()
    

###########################################################################



root=Tk()

##############CONSTRUCCION BARRA DE MENU##################################

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salir_app)

borrarMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
borrarMenu.add_command(label="Borrar campos", command=limpiar_campos)

crudMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerac de...")

###########################################################################
###########################################################################
#################COMIENZO DE CAMPOS VACIOS X RELLENAR######################

miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1,padx=10,pady=10)

cuadroNOMBRE=Entry(miFrame, textvariable=miNombre)
cuadroNOMBRE.grid(row=1, column=1,padx=10,pady=10)
cuadroNOMBRE.config(fg="black", justify="right")

cuadroAPELLIDO=Entry(miFrame, textvariable=miApellido)
cuadroAPELLIDO.grid(row=2, column=1,padx=10,pady=10)

cuadroPASS=Entry(miFrame, textvariable=miPass)
cuadroPASS.grid(row=3, column=1,padx=10,pady=10)
cuadroPASS.config(show="*")

cuadroDIRECCION=Entry(miFrame, textvariable=miDireccion)
cuadroDIRECCION.grid(row=4, column=1,padx=10,pady=10)

textoCOMENTARIO=Text(miFrame, width=16, height=5)
textoCOMENTARIO.grid(row=5, column=1,padx=10,pady=10)
scrollVert=Scrollbar(miFrame, command=textoCOMENTARIO.yview)
scrollVert.grid(row=5, column=2,sticky="nsew")
textoCOMENTARIO.config(yscrollcommand=scrollVert.set)

#######################LABEL###############################################

idLabel=Label(miFrame, text="Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady="10")

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady="10")

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady="10")

passLabel=Label(miFrame, text="Pass: ")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady="10")

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady="10")

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady="10")

##########################################################################
##########################################################################

####################BOTONES INFERIORES####################################

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Leer",command=leer)
botonLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar")
botonActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar",command=limpiar_campos)
botonBorrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)

###########################################################################
root.mainloop()
