from distutils.log import error
from tkinter import *
from tkinter.scrolledtext import ScrolledText

from more_itertools import first
from bd.funcionesBD import consultar_resultados, resultados_totales


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

def mostrar_estadisticas(campo_texto):
    campo_texto.delete("1.0", END)
    aciertos, errores = consultar_resultados()
    total = aciertos + errores
    cadena = "\n----------------------------------------\n"
    campo_texto.insert(INSERT, cadena)
    cadena = "ESTADÍSTICAS\n"
    campo_texto.insert(INSERT, cadena)
    cadena = "----------------------------------------\n"
    campo_texto.insert(INSERT, cadena)
    cadena = "{:<25} {:<5}\n".format('Multiplicaciones: ', total)
    campo_texto.insert(INSERT, cadena)
    cadena = "{:<25} {:<5} {:<5} {:<0} \n".format('Aciertos: ', aciertos, round((aciertos/total)*100, 2), "%")
    campo_texto.insert(INSERT, cadena)
    cadena = "{:<26} {:<5} {:<4} {:<0}\n".format('Errores: ', errores, round((errores/total)*100, 2), "%")
    campo_texto.insert(INSERT, cadena)
    cadena = "----------------------------------------\n"
    campo_texto.insert(INSERT, cadena)


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
    #---------------------------MiFrame2--------------------------------
    boton_label = Label(miFrame2, text="")
    boton_label.grid(row=0,column=0, sticky="w",pady=5)
    
    boton_clear = Button(miFrame2, text="Clear", background="#D6EAF8",  command=lambda:campo_texto.delete("1.0", END))
    boton_clear.grid(row=1,column=0, sticky="e", pady=5, padx =30)
    boton_clear.config(width=15)
    boton_clear.config(cursor="hand2")

    boton_resul = Button(miFrame2, text="Resultado", background="#D6EAF8",  command=lambda:mostrar_resultado(campo_texto))
    boton_resul.grid(row=2,column=0, sticky="e", pady=5, padx =30)
    boton_resul.config(width=15)
    boton_resul.config(cursor="hand2")

    boton_estad = Button(miFrame2, text="Estadística", background="#D6EAF8",  command=lambda:mostrar_estadisticas(campo_texto))
    boton_estad.grid(row=3,column=0, sticky="e", pady=5, padx =30)
    boton_estad.config(width=15)
    boton_estad.config(cursor="hand2")

    boton_mod = Button(miFrame2, text="Modificar", background="#D6EAF8",  command='')
    #boton_mod.grid(row=4,column=0, sticky="e", pady=5, padx =30)
    boton_mod.config(width=15)
    boton_mod.config(cursor="hand2")
    

