#ejemplo diccionario
estudiante = { 
    "nombre": "Maria Lopez",
    "edad" : 22,
    "carrera ": "Ingenieria Informatica",
    "promedio" : 8.5,
    "materias aprobadas": ["Programacion", "Matematicas","Base de Datos"]
}
# preguntar una clave
print(estudiante["nombre"])
print(estudiante.get("edad", "No Existe"))
print(estudiante.get( "casa", "No existe"))
estudiante ["edad"] = 23
estudiante["Universidad"] = "Los Lagos"
print(estudiante.values())

for nuevo in estudiante:
    print(f"{nuevo}: {estudiante [nuevo]}")

for nuevo, valor in estudiante.items():
    print(f"{nuevo} -> {valor}")



