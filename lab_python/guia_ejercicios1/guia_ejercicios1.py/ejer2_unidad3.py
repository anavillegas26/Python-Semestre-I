'''Se tiene que crear un programa que permita registrar las notas de estudiantes de una 
asignatura. Todos los datos (número de estudiantes, nombre de la asignatura, nombres de los 
estudiantes y sus 3 calificaciones) se ingresan por consola'''
''' Requisitos del algoritmo:
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
 ● Calcular el promedio de las 3 notas para cada estudiante.'''

# 1 Solicitud de cantidad de estudiantes
while True:
    try:
        cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes a registrar: "))
        if cantidad_estudiantes < 1:
            raise ValueError("Debe ingresar un número entero positivo mayor que cero.")
        break
    except ValueError as e:
        print(f"Error: {e}")

# 2. Registro asignatura
asignatura = input("Ingrese el nombre de la asignatura: ")
registros = []

for i in range(cantidad_estudiantes):
    print(f"\n Estudiante {i + 1}:")
    nombre = input("Nombre del estudiante: ")
    
    notas = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese nota {j + 1}: "))
                if 0.0 <= nota <= 7.0:
                    notas.append(nota)
                    break
                else:
                    raise ValueError("La nota debe estar entre 0.0 y 7.0.")
            except ValueError as e:
                print(f"Error: {e}")

    promedio = round(sum(notas) / 3, 2)
    registros.append({
        "Nombre": nombre,
        "Notas": notas,
        "Promedio": promedio
    })

# Resultados finales
print(f"\n Resultados de la asignatura: {asignatura}\n")
for estudiante in registros:
    print(f"{estudiante['Nombre']}: Notas = {estudiante['Notas']} | Promedio = {estudiante['Promedio']}")


