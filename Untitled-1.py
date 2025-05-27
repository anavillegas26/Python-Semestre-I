
#INICIANDO VARIABLE NUMERICAS
edad = 31
estatura = 1.71
peso = 75.4
complejo = 2 + 9j # INICIANDO UN NUMERO COMPLEJO
complejo2 = complex (1,4)

#IMPRESION NUMEROS COMPLEJOS
print (complejo)
print (complejo2)

#operacion aritmetica
imc = peso / (estatura **2)
print (f"su IMC es: {imc}")

#FORMATO DE SALIDA DEL RESULTADO (UTILIZANDO F- STRINGS Y :2f)
print(f"Su IMC es:{imc:.2f}")# salida con 2 decimales

#FORMATO DE SALIDA DEL RESULTADO (UTILIZANDOEL METODO FORMAT)
print ("Su IMC es: {:.2f}". format(imc))

#TRANDFORMANDO UN NUMERO ENTERO EN UN NUMERO FLOTANTE
print(float(edad))

#04 - DATOS DE TIPO STRING (CADENAS DE TEXTO)
carrera = 'Ingeniería Civil en Informática'
asignatura = "Programación"
descripcion = '''Esta es una asignatura
de primer semestre '''

#APLICANDO EL METODO SPLIT (GENERA UN ARREGLO DE CADENA)
print(descripcion.split())

#ARREGLO NUMERICO 






 