
#creando dicccionario # se pueden agregar diferentes datos estructurados
paciente = {'nombre':'carlos',
            'apellido':'santana',
              'edad':'50',
              'ciudad':'quellon'}

#OTRA FORMA DE DECLARAR DICCIONARIO
medico = dict (
    nombre = 'samir',
    apellido = 'arana',
    edad =20,
    especialidad = 'neurologo')

#impresiion diccionario
print (paciente)
print(medico)

# consultando un elemento a traves de la clave del diccionario
print(medico["nombre"])

#eliminando una clave del diccionario
del(paciente['nombre'])
print(paciente)
