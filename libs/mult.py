from time import sleep
from random import randint, shuffle
import os
import threading


def continuar(pasar):
    while not pasar.get():
        #print("pasar: ", pasar.get())
        sleep(0.1)
    #print("Pasar Actualizado: ", pasar.get())

def comenzar(total, texto, resultado, pasar, texto_multi, mul, tablas):
    t1 = threading.Thread(target =   multiplicar, args = (total,texto, resultado, pasar, texto_multi, mul, tablas), daemon = True)
    t1.start()

def multiplicar(total, texto, resultado, pasar, texto_multi, multi, tablas_chk):
    tab = tablas_chk
    #print(tablas_chk)
    #tablas = [2,3,4,5]
    tablas = [i+2 for i in range(len(tablas_chk)) if tablas_chk[i] is True]
    #print(tablas)
    try:
        num = total.get()
    except:
        num = 0

    texto.set("")
    mul = 1
    error = 0
    errores = 0
    while mul <= num:
        try:
            shuffle(tablas)
            a = tablas[randint(0, len(tablas)-1)]
            c= [i for i in range(2,10)]
            shuffle(c)
            b = c[randint(0, len(c)-1)]
            texto_multi.set(f"{a}x{b}")
            multi.set(f"Multiplicaciones: {mul}")
            #cmd = resultado.bind("<Return>",resultado.get())
            #cmd = int(resultado.get())
            fin_cuenta = False
            while not fin_cuenta:
                texto.set("")
                continuar(pasar)
                if int(resultado.get()) == a * b:
                    path = os.getcwd()+ "\\files\\aciertos.txt"
                    escribir_fichero(f"{a}x{b}", path)
                    texto.set("¡¡Bien!!")
                    sleep(1)
                    fin_cuenta = True
                    mul += 1
                    error = 0
                 
                else:
                    path = os.getcwd()+ "\\files\errores.txt"
                    escribir_fichero(f"{a}x{b}", path)
                    errores += 1
                    if error == 1:
                        texto.set("Dejate de rollo Carmen y no la cagues más")
                        sleep(1)
                        error -= 1
                    else:
                        texto.set(f"Lo siento te has equivocado, intentalo otra vez")
                        sleep(1)
                        error += 1
                pasar.set(False)
                resultado.set("")
        
                   
        except:
            texto.set("Dejate de rollo Carmen y sigue multiplicando")
            sleep(1)
            pasar.set(False)
            resultado.set("")
        
    total.set("")
    if num > 0:
        texto_multi.set(f"Errores: {errores}")
        texto.set(f"Multiplicaciones: {num}")
    else:
        texto_multi.set(f"Introduce número de")
        texto.set(f"Multiplicaciones")

def escribir_fichero(string, path):
    print(path)
    file = open(path, "a")
    file.write(string+"//")
    file.close()
    print("fichero escrito")