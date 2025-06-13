entrada = input("Ingrese un valor entero")
import os
    print("Directorio de trabajo actual:", os.getcwd()) # muestra la abicacion del directorio actual
try:
    numero = int (entrada)
    print(f"Numero ingresad: {numero}")
except ValueError:
    print("Error de valor: el valor ingresado no es entero")
except Exception as e:           # lo va guardar como una variable e
    print(f"Error inesperado :{e}")
else:
    print("Conversion fue exitosa")
finally:    #acccion de limpieza cerrar el archivo si esta abierto
    print("Finalizacion del bloque")

    


