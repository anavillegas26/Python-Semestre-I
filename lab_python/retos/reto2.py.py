
 
# crea inventario
inventario = {
    "Manzana": (900, 950, 920),
    "Platano": (500, 500, 550),
    "Cereza": (1200, 1250, 1300)
}

#  precios del plátano 
precios_platano = set(inventario["Platano"])

# Convertir set a lista 
precios_platano = list(precios_platano)

# Lista con  tipos de frutas
tipos_frutas = list(inventario.keys())

# Calcular promedio 
promedio_platano = round(sum(precios_platano) / len(precios_platano), 3)

#  resultados
print("Inventario completo:")
print(inventario)

print("\n Precios únicos del plátano:")
print(precios_platano)

print("\n Tipos de frutas registradas:")
print(tipos_frutas)

print("\n Promedio de precios únicos del plátano:")
print(f"${promedio_platano}")




 
