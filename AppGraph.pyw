
from tkinter import *
from tkinter import messagebox
from xmlrpc.client import Boolean
from libs.mult import *
from libs.clases import *


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

tab2 = BooleanVar()
tab3 = BooleanVar()
tab4 = BooleanVar()
tab5 = BooleanVar()
tab6 = BooleanVar()
tab7 = BooleanVar()
tab8 = BooleanVar()
tab9 = BooleanVar()
tab10 = BooleanVar()


#----------------------Funciones---------------------------------------------
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
tab2.set(True)
tab3.set(True)
tab4.set(True)
tab5.set(True)
#-----------------------------Menu-----------------------------------

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_command(label="Salir", command=salirAplicacion)


#-------------------Frames-----------------------------
#----------------------miFrame--------------------------
multiplicar_boton=Button(miFrame, text="Comenzar", background="#D5DBDB",  command=lambda:comenzar(total, texto, resultado, pasar, texto_multi, mul, tablas_chk.state()))
multiplicar_boton.grid(row=0,column=0, sticky="w",columnspan=1, pady=10, padx =3)
multiplicar_boton.config(width=33)
multiplicar_boton.config(cursor="hand2")

resultados=Button(miFrame, text="Resultados", bg = '#85929E', command=lambda x:x)
resultados.grid(row=0,column=1, sticky="e",columnspan=1, pady=10, padx =3)
resultados.config(width=33)
resultados.config(cursor="hand2")

#----------------------miFrameTablas-------------------------

tablas = Label(miFrameTab, text = 'Tablas:')
tablas.grid(row=0,column=0, sticky="w",pady=5)
'''
t2 = Checkbutton(miFrameTab, text='2',variable=tab2)
t2.grid(row=1,column=0)
t3 = Checkbutton(miFrameTab, text='3',variable=tab3)
t3.grid(row=1,column=1)
t4 = Checkbutton(miFrameTab, text='4',variable=tab4)
t4.grid(row=1,column=2)
t5 = Checkbutton(miFrameTab, text='5',variable=tab5)
t5.grid(row=1,column=3)
t6 = Checkbutton(miFrameTab, text='6',variable=tab6)
t6.grid(row=1,column=4)
t7 = Checkbutton(miFrameTab, text='7',variable=tab7)
t7.grid(row=1,column=5)
t8 = Checkbutton(miFrameTab, text='8',variable=tab8)
t8.grid(row=1,column=6)
t9 = Checkbutton(miFrameTab, text='9',variable=tab9)
t9.grid(row=1,column=7)
t10 = Checkbutton(miFrameTab, text='10',variable=tab10)
t10.grid(row=1,column=8)
'''
tablas_chk = Checkbar(miFrameTab, [str(i) for i in range(2,11)])
tablas_chk.grid(row=1,column=0)

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

mult_real = Label(miFrame1, textvariable = mul, background="#76D7C4")
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

