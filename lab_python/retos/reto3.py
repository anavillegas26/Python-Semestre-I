''' Obtener e imprimir los numeros del rango mayor o igual del 500 al 100, incrementando de 3 en 3
A continuacion, sumar todos los numeros obtenidos, y obtener el promedio de todos los numeros,
mostrar el resultado en consola'''

numeros = list(range( 500,99, -3))
print(numeros)

#calcular suma de numeros
suma = sum(numeros)
print(f"La suma de los numeros es:{suma}")

#calcular el promedio

promedio = suma/ len(numeros)
print(f"El promedio es: {promedio}")