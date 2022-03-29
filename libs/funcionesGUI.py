from tkinter import *
from tkinter.scrolledtext import ScrolledText

from more_itertools import first
from bd.funcionesBD import resultados_totales


def mostrar_resultado(campo_texto):
    campo_texto.delete("1.0", END)
    insertar_cabecera(campo_texto)
    consulta = resultados_totales()
    for resultado in consulta:
        cadena = "            {:<10} {:<10} {:<10}\n".format(resultado[0], resultado[1], resultado[2])
        campo_texto.tag_config('justified', justify=CENTER)
        campo_texto.insert(INSERT, cadena)
        cadena = "----------------------------\n"
        campo_texto.tag_config('justified', justify=CENTER)
        campo_texto.insert(INSERT, cadena, 'justified')

def insertar_cabecera(campo_texto):
    cabecera = "{:<7} {:<10} {:<5}\n".format('MULT','ACIERTOS','ERRORES')
    #texto.set(cabecera)
    
    campo_texto.tag_config('justified', justify=CENTER)
    campo_texto.insert(INSERT, cabecera, 'justified')
    cabecera = "----------------------------\n"
    #texto.set(cabecera)
    campo_texto.tag_config('justified', justify=CENTER)
    campo_texto.insert(INSERT, cabecera, 'justified')


def ventana_resultados():
    ventana_resultados = Toplevel()
    ventana_resultados.iconbitmap("./images/logo.ico")
    ventana_resultados.title("Resultados")
    #--------------------------Frame-----------------------------------
    miFrame=Frame(ventana_resultados)
    miFrame.grid(row=0,column=0,columnspan=1,sticky="nw")
    miFrame.config(bd=2)

    miFrame2=Frame(ventana_resultados)
    miFrame2.grid(row=0,column=1,columnspan=1,sticky="nw")
    miFrame2.config(bd=2)

    #-------------------------Veriables--------------------------------
    texto = StringVar()
    #------------------------------------------------------------------
    resul_label = Label(miFrame, text="Resultados:")
    resul_label.grid(row=0,column=0, sticky="w",pady=5)

    campo_texto = ScrolledText(miFrame, width=50, height=10)
    campo_texto.grid(row=1, column=0)

    boton_resul = Button(miFrame2, text="Resultado", background="#D6EAF8",  command=lambda:mostrar_resultado(campo_texto))
    boton_resul.grid(row=1,column=0, sticky="e", pady=5, padx =30)
    boton_resul.config(width=15)
    boton_resul.config(cursor="hand2")
    

