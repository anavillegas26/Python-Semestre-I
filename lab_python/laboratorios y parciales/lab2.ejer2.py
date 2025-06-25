# ingresar un texto
resumen = input("Ingresar resumen de texto \n > ")
print(resumen)
 
limite = len(resumen) <= 50 # indica si es true o false 
print(limite)

longitud = len(resumen)

print(f"La longitud  es:{longitud} \n") # longitud

print(f"El resumen en mayusculas es: {resumen.upper() }\n") # resumen en mayusculas

print(f"El resumen en minusculas es: {resumen.lower()}\n")# resumen en minusculas

print(f"El numero de veces que aparece la vocal e es: {resumen.count("e")}\n") # contar las letas e

print(resumen[-15:-1])

print(resumen[0:15])

print(resumen.split())

