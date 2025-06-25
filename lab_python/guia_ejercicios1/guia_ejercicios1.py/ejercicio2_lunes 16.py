'''Se tiene que crear un programa que permita registrar las notas de estudiantes de una 
asignatura. Todos los datos (número de estudiantes, nombre de la asignatura, nombres de los 
estudiantes y sus 3 calificaciones) se ingresan por consola.
 Requisitos del algoritmo:
 1. Solicitud de cantidad de estudiantes
 ● Pedir al usuario cuántos estudiantes desea registrar (entero positivo).
 ● Si la entrada no es un entero válido o es menor que 1, capturar la excepción y 
volver a solicitar.
 2. Registro de datos
 ● Leer el nombre de la asignatura.
 ● Para cada uno de los N estudiantes:
 ○ Leer su nombre.
 ○ Leer sus 3 notas (flotantes entre 0.0 y 7.0), validando rango y 
formato; ante error, capturar la excepción y pedir de nuevo cada 
nota.
 3. Cálculo de promedios
 ● Calcular el promedio de las 3 notas para cada estudiante'''
 # solicitar numero de estudiantes con manejo de excepcione
num_estudiantes = int(input("Ingresar cantidad de estudiantes"))
if num_estudiantes < 1 :
    raise ValueError ("Debe ser un entero positivo")
try:
    cant_estudiantes = int(num_estudiantes)
    print(f"Cantidad de estudiantes:{cant_estudiantes}")
except ValueError:
    print('¡Error! no es entero positivo.')

except Exception as e:
    print(f"Error inesperado:{e}")
else:
    print("Objetivo completado")
finally:
    print("Ahora registre sus otros datos")

asignatura =input(" Ingrese la asignatura")
num_estud1 = input("Ingrese el nombre del estudiante")
notas = float(input("ingrese las notas"))
if notas 0 > and < 7.0 :
   try:
       notas = float(notas)
