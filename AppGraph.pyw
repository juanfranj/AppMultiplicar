
from tkinter import *
from tkinter import messagebox
from xmlrpc.client import Boolean
from libs.funcionesGUI import *
from libs.mult import *
from libs.clases import *


root=Tk()


#---------------Introduco el titulo y el logo del software-------------
root.iconbitmap("./images/logo.ico")
root.title("Multiplications")
#root.config(width=400, height=400, bg ='#D0ECE7')
#root.config(bg ='#D0ECE7')


#---------------Introduzco el Frame-----------------------------------
miFrame=Frame(root)
miFrame.grid(row=0,column=0,columnspan=2,sticky="nw")
miFrame.config(bd=2)
#miFrame.config(relief="groove")

miFrame1=Frame(root)
miFrame1.grid(row=2,column=0,columnspan=2,sticky="nw")
miFrame1.config(bd=2)
#miFrame1.config(relief="groove")

miFrame2=Frame(root)
miFrame2.grid(row=3,column=0,columnspan=2,sticky="nw")
miFrame2.config(bd=3)
miFrame2.config(relief="groove")

miFrame3=Frame(root)
miFrame3.grid(row=4,column=0,columnspan=2,sticky="nw")
miFrame3.config(bd=2)
#miFrame3.config(relief="groove")

miFrameTab = Frame(root)
miFrameTab.grid(row=1 ,column=0,columnspan=2,sticky="nw")
miFrameTab.config(bd=2)

FramePrueba =  Frame(root)
FramePrueba.grid(row=5 ,column=0,columnspan=2,sticky="nw")
FramePrueba.config(bd=2)
#-------------------------Variables------------------------------
total = IntVar()
texto_multi = StringVar()
texto = StringVar()
resultado = IntVar()
pasar = BooleanVar()
mul   = StringVar()

#----------------------Funciones---------------------------------------------
def onEnter(event):
    actualizar_pasar()

def actualizar_pasar():
    if pasar.get():
        pasar.set(False) 
    else:
        pasar.set(True)

def salirAplicacion():
	valor=messagebox.askokcancel("Salir","Carmen, recuerda que tu Papi te quiere mucho.\n            ¿Deseas salir de la aplicación?")
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
multiplicar_boton=Button(miFrame, text="Comenzar", background="#A2D9CE",  command=lambda:comenzar(total, texto, resultado, pasar, texto_multi, mul, tablas_chk.state(), False))
multiplicar_boton.grid(row=0,column=0, sticky="w",columnspan=1, pady=10, padx =3)
multiplicar_boton.config(width=23)
multiplicar_boton.config(cursor="hand2")

errores=Button(miFrame, text="Errores", bg = '#F5B7B1', command=lambda:comenzar(total, texto, resultado, pasar, texto_multi, mul, tablas_chk.state(), True))
errores.grid(row=0,column=1, sticky="e",columnspan=1, pady=10, padx =3)
errores.config(width=23)
errores.config(cursor="hand2")

resultados=Button(miFrame, text="Resultados", bg = '#5499C7', command=lambda:ventana_resultados(root))
resultados.grid(row=0,column=2, sticky="e",columnspan=1, pady=10, padx =3)
resultados.config(width=23)
resultados.config(cursor="hand2")

#----------------------miFrameTablas-------------------------

tablas = Label(miFrameTab, text = 'Tablas:')
tablas.grid(row=0,column=0, sticky="w",pady=5)

tablas_chk = Checkbar(miFrameTab, [str(i) for i in range(2,11)])
tablas_chk.grid(row=1,column=0)

clear=Button(miFrameTab, text="Clear", background="#D6EAF8",  command=lambda: [i.set(False) for i in tablas_chk.vars])
clear.grid(row=1,column=1, sticky="e", pady=5, padx =30)
clear.config(width=15)
clear.config(cursor="hand2")


#tablas_chk.pack(side=TOP, fill=X)
#--------------------FramePrueba------------------------
#lng = Checkbar(FramePrueba, ['Python', 'Ruby', 'Perl', 'C++'])
#lng.pack(side=TOP,  fill=X)
#print(list(lng.state()))
#----------------------miFrame1-------------------------


total_mult=Label(miFrame1, text="Nº multiplicaciones:")
total_mult.grid(row=2,column=0,sticky="w",pady=10, padx=10)

total_entry=Entry(miFrame1, text=total, justify=RIGHT)
total_entry.grid(row=2,column=1, sticky="e")
total_entry.config(width=5)

mult_real = Label(miFrame1, textvariable = mul, background="#D6DBDF")
mult_real.grid(row=2,column=2, sticky="e",pady=10, padx=10)
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

