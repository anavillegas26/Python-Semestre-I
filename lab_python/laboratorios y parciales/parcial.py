
#  A Crear el diccionario de gatitos

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

print("Diccionario inicial de gatitos:\n")

for ingreso, datos in gatitos.items():
    print(f"{ingreso}: {datos}")

#  B Clasificación según peso
for datos in gatitos.values():
    peso = datos["Peso"]
    if peso < 1:
        datos["Clasificación-Peso"] = "Bajo Peso"
    elif 1 <= peso <= 4:
        datos["Clasificación-Peso"] = "Normal"
    else:
        datos["Clasificación-Peso"] = "Sobre Peso"

# C: Categoría etaria 
for datos in gatitos.values():
    try:
        edad = datos["Edad"]
        if edad < 4:
            datos["Categoría-Etaria"] = "Cachorro"
        elif 4 <= edad <= 12:
            datos["Categoría-Etaria"] = "Joven"
        else:
            datos["Categoría-Etaria"] = "Adulto"
    except:
        datos["Categoría-Etaria"] = "Desconocida"


print("\nDiccionario actualizado con clasificación de peso y categoría etaria:\n")
for ingreso, datos in gatitos.items():
    print(f"{ingreso}: {datos}")


# D) Lista de tuplas 
lista_pesos = sorted([(ingreso, datos["Peso"]) for ingreso, datos in gatitos.items()],
                     key=lambda x: x[1])
print("\nLista ordenada por peso (menor a mayor):")
for ingreso, peso in lista_pesos:
    print(f"Ingreso: {ingreso}, Peso: {peso} kg")

# E) Ingreso de nuevos gatitos ---
while True:
    try:
        ingreso = int(input("\nIngrese el N° de Ingreso del nuevo gatito: "))
        nombre = input("Nombre: ")
        peso = float(input("Peso (kg): "))
        edad = int(input("Edad (meses): "))
        tamaño = int(input("Tamaño (cm): "))

        gatitos[ingreso] = {
            "Nombre": nombre,
            "Peso": peso,
            "Edad": edad,
            "Tamaño": tamaño
        }

        # Opcional: clasificaciones automáticas para los nuevos
        if peso < 1:
            gatitos[ingreso]["Clasificación-Peso"] = "Bajo Peso"
        elif peso <= 4:
            gatitos[ingreso]["Clasificación-Peso"] = "Normal"
        else:
            gatitos[ingreso]["Clasificación-Peso"] = "Sobre Peso"

        try:
            if edad < 4:
                gatitos[ingreso]["Categoría-Etaria"] = "Cachorro"
            elif edad <= 12:
                gatitos[ingreso]["Categoría-Etaria"] = "Joven"
            else:
                gatitos[ingreso]["Categoría-Etaria"] = "Adulto"
        except:
            gatitos[ingreso]["Categoría-Etaria"] = "Desconocida"

        continuar = input("¿Desea agregar otro gatito? (s/n): ").lower()
        if continuar != 's':
            break

    except ValueError:
        print("Datos inválidos. Intente nuevamente.")

#  F Actualizar tamaño de un gatito existente 
try:
    num_ingreso = int(input("\nIngrese el N° de ingreso del gatito a modificar: "))
    if num_ingreso in gatitos:
        nuevo_tamaño = int(input("Nuevo tamaño (cm): "))
        gatitos[num_ingreso]["Tamaño"] = nuevo_tamaño
        print(" Tamaño actualizado correctamente.")
    else:
        print(" No se encontró ese número de ingreso.")
except ValueError:
    print("⚠️ Entrada inválida.")

# G) Estadísticas de pesos 
pesos = [datos["Peso"] for datos in gatitos.values()]
promedio = sum(pesos) / len(pesos)
peso_max = max(pesos)
peso_min = min(pesos)
ingreso_min_peso = min(gatitos.items(), key=lambda item: item[1]["Peso"])[0]

print("\n Estadísticas de peso:")
print(f"Promedio: {promedio:.2f} kg")
print(f"Máximo: {peso_max} kg")
print(f"Mínimo: {peso_min} kg")
print(f"N° de ingreso con menor peso: {ingreso_min_peso}")

# --- Impresión final del diccionario
print("\n Registro final de gatitos (ordenado por ingreso):")
for ingreso in sorted(gatitos):
    print(f"{ingreso}: {gatitos[ingreso]}")
