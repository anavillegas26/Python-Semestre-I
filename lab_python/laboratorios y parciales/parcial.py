# crear diccionario

gatitos = {
    101 : {
        "Nombre":"Luna",
        "Peso" :1.2,
        "Edad": 3,
        "Tamaño": 30},
    102 :{
        "Nombre":"Michi",
        "Peso" :0.8,
        "Edad": 2,
        "Tamaño": 25
        },
    103 :{
        "Nombre":"Pepito",
        "Peso" :2.5,
        "Edad": 5,
        "Tamaño": 35}
     }

    

print(gatitos)


for i in gatitos:
       i == 1.2
    
for peso_Luna in gatitos:
    peso_Luna < 1 
    print("El Gatito esta Bajo Peso")
else:
    1 <- peso_Luna <-4 
    print("El Gatito esta en Peso Normal")

gatitos[101]["Peso"]
gatitos[101]["Clasificación"]="Normal" # agregar al diccionario la clasificacion


peso_Michi= 0.8
for peso_Michi in gatitos:
    peso_Michi < 1 
    print("El Gatito esta Bajo Peso")
else:
    1 <- peso_Michi <-4 
    print("El Gatito esta en Peso Normal")

gatitos[102]["Peso"]
gatitos [102]["Clasificación"]= "Bajo Peso"


peso_Pepito = 2.5
for peso_Pepito in gatitos:
    peso_Pepito < 1 
    print("El Gatito esta Bajo Peso")
else:
    1 <- peso_Pepito <-4 
    print("El Gatito esta en Peso Normal")

gatitos[103]["Peso"]   
gatitos[103]["Clasificación"]= "Normal"

# crea lista de tuplas
numero_ingreso = (101,102,103)
peso = (1.2,0.8,2.5)
mayor= list(numero_ingreso + peso)
print(mayor)

# Crear una lista con todos los valores de "Peso", y luego calcular e imprimir:


peso1 = (1.2,0.8,2.5)
promedio = sum(peso1) /5
print(promedio)

max_peso= max(peso1)
print(max_peso)

min_peso=min(peso1)
print(min_peso)


''' Crear otro bucle para agregar la clave "Categoría-Etaria" basada en la edad: (10 Pts)
● < 4 meses → "Cachorro"
● 4 ≤ edad ≤ 12 meses → "Joven"
● > 12 meses → "Adulto"
Dentro del bucle, utilizar un try/except para asignar "Desconocida" si ocurre un error al
ingresar una edad no válida.'''


for i in  gatitos:
    i < 4  

