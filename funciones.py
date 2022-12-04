from tkinter import *
from tkinter import messagebox
import sqlite3
# from codigo import *



# def conexionBBDD():
#     miConexion=sqlite3.connect('pild_infor_59/Usuarios')
#     miCursor=miConexion.cursor()
#     try:
#         miCursor.execute('''
#             CREATE TABLE DATAUSUARIOS(
#             ID INTEGER PRIMARY KEY AUTOINCREMENT,
#             NOMBRE_USUARIO VARCHAR(50),
#             PASSWORD VARCHAR(50),
#             APELLIDO VARCHAR(10),
#             DIRECCION VARCHAR(50),
#             COMENTARIOS VARCHAR(100)) 
#             ''')
#         messagebox.showinfo("BBDD", "BBDD creada con exito")
#     except:
#         messagebox.showwarning("¡Atencion!", "La BBDD ya existe")
        

# def limpiar_campos():
#     miNombre.set("")
#     miId.set("")
#     miApellido.set("")
#     miDireccion.set("")
#     miPass.set("")
#     textoCOMENTARIO.delete(1.0, END)

 