"""
Crear un algoritmo que permita manipular cadenas de texto: 
A. Ingresar una frase de máximo 30 caracteres. 
B. Generar dos nuevas variables: una en mayúsculas y otra en minúsculas. 
C. Utilizar un método propio para determinar cuántas veces aparece la letra «a» (tanto «a» 
como «A») en la frase, y muestra el total. 
D. Emplear otro método para imprimir la longitud de la frase original.
"""

frase = str(input("Ingresa una frase por favor:")) [0:30] # ingresando cadena de texto 

# generando texto en mayuscula y minuscula
mayuscula = frase.upper()
minuscula = frase.lower()
print(mayuscula)
print(minuscula)

#cantidad de a
cantidad_de_a = frase.count("a")
cantidad_de_A = frase.count("A")

print(cantidad_de_a)
print(cantidad_de_A)

print(f"La frase tiene: {len(frase)} caracteres")
