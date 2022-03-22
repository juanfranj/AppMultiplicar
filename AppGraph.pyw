
from tkinter import *
from tkinter import messagebox
from xmlrpc.client import Boolean
from libs.mult import *


root=Tk()


#---------------Introduco el titulo y el logo del software-------------
root.iconbitmap("./images/logo.ico")
root.title("Multiplications")
#root.config(width=400, height=400)
#---------------Introduzco el Frame-----------------------------------
miFrame=Frame(root)
miFrame.grid(row=0,column=0,columnspan=2,sticky="nw")
miFrame.config(bd=2)
#miFrame.config(relief="groove")

miFrame1=Frame(root)
miFrame1.grid(row=1,column=0,columnspan=2,sticky="nw")
miFrame1.config(bd=2)
#miFrame1.config(relief="groove")

miFrame2=Frame(root)
miFrame2.grid(row=2,column=0,columnspan=2,sticky="nw")
miFrame2.config(bd=3)
miFrame2.config(relief="groove")

miFrame3=Frame(root)
miFrame3.grid(row=3,column=0,columnspan=2,sticky="nw")
miFrame3.config(bd=2)
#miFrame3.config(relief="groove")
#-------------------------Variables------------------------------
total = IntVar()
texto_multi = StringVar()
texto = StringVar()
resultado = IntVar()
pasar = BooleanVar()
mul   = StringVar()

#-------------------------------------------------------------------
def onEnter(event):
    actualizar_pasar()

def actualizar_pasar():
    if pasar.get():
        pasar.set(False) 
    else:
        pasar.set(True)

def salirAplicacion():
	valor=messagebox.askokcancel("Salir","¿Deseas salir de la aplicación?")
	if valor==True:
		root.destroy()
#----------------------------Inicio variable----------------------
pasar.set(False)
texto.set("Hola Carmen, ¿preparada para repasar las tablas?")
total.set("")
resultado.set("")
#-----------------------------Menu-----------------------------------

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_command(label="Salir", command=salirAplicacion)


#-------------------Frames-----------------------------
#----------------------miFrame--------------------------
multiplicar_boton=Button(miFrame, text="Comenzar", background="#D5DBDB",  command=lambda:comenzar(total, texto, resultado, pasar, texto_multi, mul))
multiplicar_boton.grid(row=0,column=0, sticky="w",columnspan=1, pady=10, padx =3)
multiplicar_boton.config(width=33)
multiplicar_boton.config(cursor="hand2")

resultados=Button(miFrame, text="Resultados", bg = '#85929E', command=lambda x:x)
resultados.grid(row=0,column=1, sticky="e",columnspan=1, pady=10, padx =3)
resultados.config(width=33)
resultados.config(cursor="hand2")

#----------------------miFrame1-------------------------
total_mult=Label(miFrame1, text="Nº multiplicaciones:")
total_mult.grid(row=0,column=0,sticky="w",pady=10, padx=10)

total_entry=Entry(miFrame1, text=total, justify=RIGHT)
total_entry.grid(row=0,column=1, sticky="e")
total_entry.config(width=5)

mult_real = Label(miFrame1, textvariable = mul, background="#76D7C4")
mult_real.grid(row=0,column=2, sticky="e",pady=10, padx=10)
mult_real.config(width=43)
#---------------------miFrame2--------------------------
cuenta=Label(miFrame2, textvariable=texto_multi, justify=CENTER
    ,font = ("Helvetica", 15, "bold"))
cuenta.grid(row=0,column=0, columnspan=2, sticky="w",pady=5, padx=5)
cuenta.config(width=40)

salida=Label(miFrame2, textvariable=texto, justify=CENTER
    ,font = ("Helvetica", 15, "bold"))
salida.grid(row=1,column=0, columnspan=2, sticky="w",pady=5, padx=5)
salida.config(width=40)

#---------------------miFrame3--------------------------

resultado_label =Label(miFrame3, text="Resultado:", justify=RIGHT)
resultado_label.grid(row=1,column=0,sticky="e",pady=10, padx=5)


resultado_entry=Entry(miFrame3, text=resultado, justify=RIGHT)
resultado_entry.grid(row=1,column=1, sticky="e")
resultado_entry.config(width=5)
resultado_entry.bind('<Return>', onEnter)
















#----------------------------Fin Ventana---------------------------------
root.mainloop()

