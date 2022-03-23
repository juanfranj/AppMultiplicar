from random import randint, shuffle
import os

def tablas_multiplicar():
    tablas = [2,3,4,5]
    fin = False
    print("\n\n-------------------------TABLAS DE MULTIPLICAR------------------------\n")
    print("Cuando quieras terminar de jugar pulsa la tecla n, vale?")
    print("\nHola Carmen, ¿preparada para repasar las tablas?")
    total = int(input("\n¿Cuantas multiplicaciones quieres hacer?:"))
    print("")
    mul = 1
    error = 0
    errores = 0
    while mul <= total:
        try:
            shuffle(tablas)
            a = tablas[randint(0, len(tablas)-1)]
            c = [i for i in range(2,10)]
            shuffle(c)
            b = c[randint(0, len(c)-1)]
            cmd = input(f"Cuánto es {a}x{b}: ")
            fin_cuenta = False
            while not fin_cuenta:
                if int(cmd) == a * b:
                    print("\n¡¡Bien!!\n")
                    fin_cuenta = True
                    mul += 1
                    error = 0
                else:
                    errores += 1
                    if error == 1:
                        print("\nDejate de rollo Carmen y no la cagues más\n")
                        cmd = input(f"Cuánto es {a}x{b}: ")
                        error -= 1
                    else:
                        print("\nLo siento te has equivocado, intentalo otra vez\n")
                        cmd = input(f"Cuánto es {a}x{b}: ")
                        error += 1
                    
        except ValueError:
            print("\nDejate de rollo Carmen y sigue multiplicando\n")
    os.system("cls")
    print("\n\n\n\n\n")
    print("\n\n========================================================================================================================\n\n")
    print("                                               Adios Carmen, me ha gustado jugar contigo                                          ")
    print("\n\n========================================================================================================================")
    print(f"\n\n                                Has cometido {errores} errores de un {total} de multiplicaciones                            ")
    print("\n\n========================================================================================================================")
    input("\n\n                          Pulsa ENTER para terminar          Recuerda que tu Papi te quiere mucho."
          "\n\n========================================================================================================================")
    
    
if __name__ == '__main__':
    tablas_multiplicar()
