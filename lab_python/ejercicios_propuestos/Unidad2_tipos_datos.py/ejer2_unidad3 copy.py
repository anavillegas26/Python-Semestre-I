'''. Desarrollar un algoritmo con operaciones mixtas con números complejos: 
A. Ingresar tres valores numéricos diferentes (entero, flotante y complejo) 
B. Calcular y mostrar: 
● Potencia Compleja (Complejo y Entero) 
● Suma Mixta (Complejo y Flotante) 
● Producto Mixto (Complejo y Entero) 
● Módulo de Potencia Compleja. El módulo se realiza utilizando la función abs() 
(Variable Potencia Compleja, con 3 decimales)'''


#  ingresa tres valores numericos diferentes
entero = int(input("Ingresa un numero entero:"))
flotante = float(input("Ingresa un numero flotante:"))
complejo = complex(input("Ingresa un numero complejo:"))
 
 # se calcula la potencia compleja
potencia_compleja = complejo ** entero
print(f"potencia compleja:{potencia_compleja,}")

