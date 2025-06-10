
colores ={'azul', 'rojo','azul',' naranjo'}
colorcitos = {'azul', 'naranjo'}

#IMPRIMIENDO EL SET DE COLORES
print(colores)

# AGREGANDO UN NUEVO ELEMETO AL SET (METODO ADD)
colores.add('blanco')

#aplicando em metodo difference
diferencia = colores.difference(colorcitos)
print(diferencia)

from colorama import init, Fore # invocar biblioteca
init()

mes  =4
match mes :
    case 12 | 1|2 :
        print("Verano")
     case 3| 4|5 :
        print(" Otoño")




                                