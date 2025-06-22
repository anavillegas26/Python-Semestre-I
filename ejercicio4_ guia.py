
#  desarrollar algoritmo que permita devolver propiedad descubierta por Nicomano de Gerasa
n = 5
inicio = 1
resultados = []

# crear los grupos de numeros impares
for k in range(1, n + 1): # primer numero impar de la secuencia
    impares = [inicio + 2 * i for i in range(k)]
# calcular sumas y cubo
suma_impares = sum(impares)
cubo = k ** 3

resultados.append((k, impares, suma_impares, cubo)) #almacenar resultados

inicio = impares[-1] + 2  # actualizar el inicio para el proximo grupo

#mostrar resultados
for k, impares, suma, cubo in resultados:
    print(f"Cubo {k}3  = {cubo}:")
    print(f" Impares: {'+'. join(map(str, impares))}")
    print(f" Suma:{suma}")
    print("_" * 30)


