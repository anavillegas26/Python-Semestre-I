
#INICIANDO VARIABLE NUMERICAS
edad = 31
estatura = 1.71
peso = 75.4
complejo = 2 + 9j # INICIANDO UN NUMERO COMPLEJO
complejo2 = complex (1,4)

#IMPRESION NUMEROS COMPLEJOS
print (complejo)
print (complejo2)

#operacion aritmetica
imc = peso / (estatura **2)
print (f"su IMC es: {imc}")

#FORMATO DE SALIDA DEL RESULTADO (UTILIZANDO F- STRINGS Y :2f)
print(f"Su IMC es:{imc:.2f}")# salida con 2 decimales

#FORMATO DE SALIDA DEL RESULTADO (UTILIZANDOEL METODO FORMAT)
print ("Su IMC es: {:.2f}". format(imc))

#TRANDFORMANDO UN NUMERO ENTERO EN UN NUMERO FLOTANTE
print(float(edad))

#04 - DATOS DE TIPO STRING (CADENAS DE TEXTO)
carrera = 'Ingeniería Civil en Informática'
asignatura = "Programación"
descripcion = '''Esta es una asignatura
de primer semestre '''

#APLICANDO EL METODO SPLIT (GENERA UN ARREGLO DE CADENA)
print(descripcion.split())

#ARREGLO NUMERICO 
v = [1,2,3,4,5] #INICIANDO UN ARREGLO NUMERICO
print(v[0]) # EL VALOR DE CERO MARCA LA POSICION DEL PRIMER ELEMENTO(INDICE)

#FUNCION LEND (CONTAR CANTIDAD DE CARACTERES)
print('la palabra', carrera, len(carrera))

# VALORES BOOLEANOS
interruptor = True
ampolleta = False
print(interruptor,ampolleta)

#LISTA SOLO DE NUMEROS
n = [1,2,3,4,5]

#LISTA SE SOLO STRING - UTILIZANDO LA FUNCION LIST
ramos = list(['Programación,' 'Química','POO' 'Programación'])

#IMPRIME LA POSICION DEL PRIMER ELEMENTO DE LA LISTA (NO EL CARACTER)
print(ramos[0])

#FUNCION COUNT (CUENTA LA CANTIDAD DE CONCURRENCIAS DE UN ELEMENTO)
print(ramos.count('Programación'))

#CREANDO E INSTANCIANDO UNA TUPLA
estudiante = ('Samir', 'Matías', 'Hector')
print(estudiante.index('Samir'))

ciudad = ("osorno")
print(ciudad)

#OTRA FORMA DE INSETAR UN ELEMENTO LA FUNCION LIST


#ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA 
ramos.pop()

# ORDENANDO ELEMENTOS DE UNA LISTA 
ramos.sort()
print(ramos)

#ORDENANOD ELEMENTOS DE UNA LISTA  DE FORMA DESCEDENTE A ASCENDENTE
ramos.sort()
print(ramos)

# ORDENANDO ELEMENTOS DE UNA LISTA SEGUN SU CANTIDAD  DE CARACTERES
ramos.sort(key=len) # key es una propiedad del metodo sort y se pasa un valor que en el metodo  len
print(ramos)

#OCUPANDO  EL METODO EXTEND(EXTENDIENDO UNA LSITA A PARTIR DE OTRA)
ramitos = ['calculo', 'automatas'] #nueva lista creada
ramos.extend(ramitos)
print(ramos)

estudiante = ('Samir', 'Matías', 'Hector')

 #creando e  INSTANCIANDO TUPLAS
estudiantes = ("samir",)
#METDO ONDEX EN TUPLAS
print(estudiantes.index('carlos'))

#METODO SORTED EN TUPLAS (ORDENA ELEMENTOS EN UNA TUPLA  y lo pasa a lista)
print(sorted(estudiantes))




