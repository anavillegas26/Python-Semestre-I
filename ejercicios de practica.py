n = int(input("Ingrese la cantidad de cubos a mostrar: "))
impar_actual = 1

for i in range(1, n + 1):
    suma = 0
    print(f"{i}³ =", end=" ")
    for j in range(i):
        suma += impar_actual
        print(impar_actual, end=" + " if j < i - 1 else "")
        impar_actual += 2
    print(f"= {suma}")
