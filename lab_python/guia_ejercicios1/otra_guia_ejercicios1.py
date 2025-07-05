'''Desarrollar un programa de gestión de inventario: 
A. Ingresar el nombre de un producto y su precio unitario. 
B. Ingresar la cantidad en stock. 
C. Calcular el valor total de los productos ingresados y mostrarlo con 2 decimales. 
D. Crear una variable booleana llamada umbral, que entregue un True si el valor_total > 
100000 y False en caso contrario.. 
E. Imprimir el nombre del producto, la cantidad, el valor total y el estado umbral en un solo 
print() formateado. '''                                                                                                                             

# solicitar al usuario que ingrese los datos que necesito
print("Por f)avor ingrese el nombre del producto:")
producto =str(input())

print("por favor ingresar el valor del producto:")
valor =  int(input())
print("Por favor ingresar la cantidad de stock disponible:")

stock = int(input())

valor_total= (valor * stock)
print(f"el valor total en stock es:{valor_total:.2f}")


