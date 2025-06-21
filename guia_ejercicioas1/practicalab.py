# ejemplo con condicionales
precio_de_frutas = {
    "manzana" : 1.5,
    "banana" :0.8,
    "naranja" : 1.2,
    "uva" : 2.3,
    "mango" : 2.5,
}
fruta = input("¡Que fruta desea comprar?(manzana,banana,naranja,uva,mango):").lower()
#verifica si la fruta esta en el dic. usando condicional
if fruta in precio_de_frutas:
    print(f"El precio de {fruta} es $ {precio_de_frutas[fruta]:.2f} por kilo.")

    #condicional segun el precio
if precio_de_frutas[fruta] > 2.0:
    print("¡Esta fruta esta un poco cara!")
else:
    print(f"Lo siento no tenemos {fruta} en nuestro inventario")


# pedir una fruta al usuario
fruta_buscada = input("¡Que fruta quieres consultar?.")
try:
    precio = precio_de_frutas[fruta ]
    print(f"El precio de {fruta_buscada} es ${precio} por kilo")

    if precio > 3.0:
        print("¡ Es Cara !")

    elif precio >= 2.0 :
        print("¡ Es precio Normal!")
    else:
        print("¡ Esta barata")
except ValueError:
    print(f"Lo siento, no tenemos{fruta_buscada}")  
    print(" tenemos estas frutas:") 
    for f in precio_de_frutas:
        print(f"- {f}")
finally:
    print("Gracias por venir")
 




 
