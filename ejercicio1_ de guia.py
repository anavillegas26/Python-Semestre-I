'''Una tienda de productos tecnológicos maneja la siguiente información:
 ● Productos: Smartphone, Laptop, Tablet, Smartwatch
 ● Precios (USD): 300, 800, 150, 200
 ● Stock disponible (unidades):
 ○ Smartphone: 25
 ○ Notebook: 12
 ○ Tablet: 8
 ○ Smartwatch: 4
 Se solicita desarrollar un algoritmo que:
 1. Imprima el nombre y precio del artículo más caro y del más barato, utilizando métodos 
de Python visto en clases.
 2. Para cada artículo, muestre su categoría de precio según las siguientes condiciones:
 ● Producto Económico: precio < 200
 ● Producto Estándar: 200 ≤ precio ≤ 500
 ● Producto Premium: precio > 500
 3. Liste los artículos con stock bajo (menos de 10 unidades)'''
productos=["Smartphone","Notebook","Tablet","Smartwatch"]
valores = [300,800,150,200]
stock ={
    "Smartphone" : 25,
    "Notebook" : 12,
    "Tablet": 8,
    "Smartwatch": 4, 
}

precio_min= min(valores)
print(precio_min)

precio_max = max(valores)
print(precio_max)

prod_max =productos[valores.index(precio_max)]
print(prod_max)

prod_min = productos[valores.index(precio_min)]
print(prod_min)

for prod, precio in zip(productos,valores):
    if precio < 200:
        categoria = 'productos economicos'
        print("Este producto es economico")
    elif precio <= 500 :
        categoria = 'productor estandar'
        print("Este producto es estandar")
    else :
        categoria = 'producto premium'
        print("Este producto es premium")
    print(f"{prod}:${precio}")
print()
for prod,cantidad in stock.items():
    if cantidad < 10:
        print(f"{prod}: {cantidad} unidades en stock")
