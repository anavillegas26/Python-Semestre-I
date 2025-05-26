print ("Hola Mundo!!!")

nombre = "ana"
apellido = "villegas"

# UTILIZANDO VARIABLES EN UN PRINT CON COMAS
print ("Hola mi nombre es ", nombre, "y mi apellido es " , apellido )

# IMPRIMIENDO CON OPERADOR DE CONCATENACION
print ("Hola mi nombre es " + nombre + " y mi apellido es " + apellido  )

# IMPRIMIENDO CON F-STRINGS (CADENAS LITERALES)
print(f"Hola mi nombre es {nombre} y mi apellido es {apellido} ")

# INICIANDO MULTI VARIABLES EN UNA SOLA LINEA (NO RECOMENDADO)
ciudad, region, pais = "Castro", "Los Lagos", "Chile"
print (f"Hola soy de {ciudad}, {region}, {pais}")

# 01 Iniciando variables numericas
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







 