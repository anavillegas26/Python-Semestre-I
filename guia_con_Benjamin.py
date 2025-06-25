# Nombres de los Integrantes: Benjamin Alocilla y Ana Villegas

# desarrollar algoritmo que permita devolver propiedad descubierta por Nicomano de Gerasa
n = int(input("Ingrese la cantidad de cubos a mostrar \n>"))
inicial = 1 # primer numero impar

for i in range(1, n + 1):
    suma = 0
    secuencia = []
    for j in range(i):
        suma += inicial
        secuencia.append(inicial)
        inicial+= 2
    print(f"{i}^3 = {' + '.join(map(str, secuencia))} = {suma}")

