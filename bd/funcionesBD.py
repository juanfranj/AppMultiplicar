import sqlite3
import os

def crear_valores():
    path = os.getcwd()+'\\bd\\tablasMultiplicar.db'
    conexion = sqlite3.connect(path)
    cursor = conexion.cursor()
    for i in range(2,11):
        for j in range(2,11):
            cursor.execute("INSERT INTO MULTIPLICACIONES VALUES" 
                f"('{i}x{j}', 0,0)")
    conexion.commit()
    conexion.close()

def modificar_valor(valor,acierto):
    path = os.getcwd()+'\\bd\\tablasMultiplicar.db'
    conexion = sqlite3.connect(path)
    cursor = conexion.cursor()
    mul, aciertos, errores = consultar_valor(cursor, valor)
    if acierto:
        cursor.execute(
            f"""
            UPDATE MULTIPLICACIONES
            SET ACIERTOS = {aciertos+1}
            WHERE MULTIPLICACION = '{mul}'
            """
        )
    else:
        cursor.execute(
            f"""
            UPDATE MULTIPLICACIONES
            SET ERRORES = {errores+1}
            WHERE MULTIPLICACION = '{mul}'
            """
        )

    conexion.commit()
    conexion.close()

def consultar_valor(cursor, valor):
    cursor.execute(
        f"""
        SELECT MULTIPLICACION, ACIERTOS, ERRORES
        FROM MULTIPLICACIONES
        WHERE MULTIPLICACION = '{valor}'
        """   
    )
    consulta = cursor.fetchone()
    return consulta[0], consulta[1], consulta[2]

if __name__ == '__main__':
    modificar_valor('2x8', True)