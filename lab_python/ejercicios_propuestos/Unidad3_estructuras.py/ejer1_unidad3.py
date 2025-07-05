
'''Se solicita desarrollar un algoritmo que:
1. Imprima el nombre y precio del artículo más caro y del más barato, utilizando métodos 
de Python visto en clases.
2. Para cada artículo, muestre su categoría de precio según las siguientes condiciones:
● Producto Económico: precio < 200
● Producto Estándar: 200 ≤ precio ≤ 500
● Producto Premium: precio > 500
3. Liste los artículos con stock bajo (menos de 10 unidades)
'''
# imprime nombre y precio del los productos
productos = ['Smartphone','Notebook', 'Tablet','Smartwatch']
precios = [300, 800, 150,200]

stock = {
    'Smartphone': 25,
    'Notebook' :12,
    'Tablet':8,
   ' Smartwatch':4
}
max_precio = max(precios)
print(f"El maximo precio es:{max_precio}")
min_precio = min(precios)
print(f"El minimo precio es:{min_precio}")

for prod, precio in zip(productos,precios):
    if precio < 200:
        categoria = 'Producto Economico' 
    elif precio <= 500:
        categoria ='Producto Estandar'
    else:
        categoria ='Producto Premium'
print(f'El producto es {prod}: ${precio}')
print ()
for prod,cantidad in stock.items():
    if cantidad < 10:
        print(f'Los productos con menos de unidades son :{prod:{cantidad}} ')
