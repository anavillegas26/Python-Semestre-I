#solicitar cantidades de herramientas
martillos = int(input("Por favor ingresar la cantidad de martillos: "))
clavos = int(input("Por favor ingresar la  cantidad de clavos: "))
serrucho = int(input("Por favor ingresar la cantiadad de serruchos: "))
tornillos = int(input("Por favor ingresar la cantidad de tornillos: "))
# solicitar valores de cada herramienta
valor_martillo = float(input("Por favor ingresar unitario el valor del martillo : "))
valor_clavos = float(input("Por favor ingresar unitario el valor de los clavos: ")) 
valor_serrucho = float(input("Por favor ingresar unitario el valor del serrucho: "))
valor_tornillos =  float(input("Por favor ingresar unitario el valor del martillo: "))
#valor total de cada herramientas
total_martillo = martillos * valor_martillo
print(f"El  valor total de los martillos es : {total_martillo:.2f}")
total_clavos = clavos * valor_clavos
print(f"El valor toral de los clavos es. {total_clavos:.2f}")
total_serrucho = serrucho * valor_serrucho
print(f"El valor total de los serruchos es: {total_serrucho:.2f} ")
total_tornillos = tornillos * valor_tornillos
print(f"El valor total de los tornillos  es: {total_tornillos:.2f} ")
# suma toral del inventario de herramientas
total_subtotales = total_serrucho + total_tornillos + total_clavos + total_serrucho
# valor maximo de  entre total de herramientas
valor_max = max(total_serrucho, total_tornillos, total_clavos, total_serrucho) 
print(f"El valor maximo de todos los productos es: {valor_max}")
#valos minimo de entre total de herramientas
valor_min = min(total_serrucho, total_tornillos, total_clavos, total_serrucho) 
print(f"El valor minimo de total de productos es : {valor_min}")
# promedio del valor unitario de cada herramienta
promedio_valor_unitario = (valor_clavos + valor_martillo + valor_serrucho +valor_tornillos) /4
print(f"promedio_valor_unitario: {promedio_valor_unitario:.2f}")
#valor del iva del total del inventario de herramientas
iva = (total_serrucho + total_tornillos + total_clavos + total_serrucho *19)/100
print(f"El valor del iva es : {iva}" )