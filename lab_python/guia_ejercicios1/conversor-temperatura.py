'''crear un algoritmo que sirva de Conversor de Temperatura: 
A. Solicitar por consola una temperatura en grados Celsius (números flotantes) 
B. Calcular su equivalente en grados Fahrenheit y Kelvin utilizando las fórmulas 
correspondientes. 
C. Mostrar los tres valores en pantalla, redondeados a 2 decimales.'''


grados_celsius = float(input("Ingresa los grados Celsius:")) # solicitando por consola la temperaturaen grados Celsius

grados_fahrenheit = (grados_celsius * 1.8) +  32 #equivalente en fahrenheit

grados_kelvin = grados_celsius + 273.15 # equivalente en kelvin

# mostrando  los tres valores
print(round(grados_celsius,2)) 
print(round(grados_fahrenheit,2))
print(round( grados_kelvin,2))


