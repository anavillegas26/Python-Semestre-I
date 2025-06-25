#ejercicio 3 , 3 vendedores registran sus ventas durante 5 días
sueldo_base = 529000
# crear un diccionario con las venta de 5 dias
ventas_diarias = {
    "Marta":[120000,80000,110000,80000,100000],
    "Cristian":[300000,460000,330000,250000,200000],
    "Erick":[220000,130000,280000,200000,400000]
}       
print(ventas_diarias) 
# suma el total semanal de ventas de cada vendedor
ventas_totales_M= (sum(ventas_diarias["Marta"]))
ventas_totales_C= (sum(ventas_diarias["Cristian"]))
ventas_totales_E= (sum(ventas_diarias["Erick"]))

print(f"El total de ventas semanales de Marta es: {ventas_totales_M}")
print(f"El total de ventas semanales de Cristian es: {ventas_totales_C}")
print(f"El total de ventas semanales de Erick es: {ventas_totales_E}")

#calcular el total de ventas de cada vendedor y si le corresponde bono  por ventas

try:
    if ventas_totales_M > 1500000:
        bono1 =( sueldo_base * 20) /100
    elif ventas_totales_M > 1000000:
        bono1 = (sueldo_base * 10) / 100
    elif ventas_totales_M > 500000:
        bono1= (sueldo_base * 5) / 100
    else:
        bono1= 0
        print()
finally:
    print(f"Marta recibe un bono de ${bono1:.0f}")

try:
    if ventas_totales_E > 1500000:
        bono2 =(sueldo_base * 20) / 100
    elif ventas_totales_E> 1000000:
        bono2 = (sueldo_base * 10) / 100
    elif ventas_totales_E > 500000:
        bono2= ( sueldo_base * 5) / 100
    else: 
        bono2= 0
        print(bono2)
finally:
    print(f"Erick recibe un bono de ${bono2:.0f}")      

try:
    if ventas_totales_C > 1500000:
        bono3 =(sueldo_base * 20) /100
    elif ventas_totales_C> 1000000:
        bono3 = (sueldo_base * 10 )/100
    elif ventas_totales_C> 500000:
        bono3 = (sueldo_base * 10 )/100
    else: 
        bono3 = 0
        print(bono3)
finally:
    print(f"Cristian recibe un bono de ${bono3:.0f}")

# promedio semanal de ventas de cada vendedor

promedio_ventas_M = int(ventas_totales_M / 5)
print(f"El promedio de ventas semanales de Marta es: {promedio_ventas_M}")
promedio_ventas_E = int(ventas_totales_E / 5)
print(f"El promedio de ventas semanales de Erick es: {promedio_ventas_E} ") 
promedio_ventas_C = int(ventas_totales_C / 5)
print(f"El promedio de ventas semanales de Cristian es: {promedio_ventas_C} ")

# imprime el reposte con el sueldo de cada vendedor mas el bono correspondiente
sueldo_Marta = (sueldo_base + bono1)
print(f"El sueldo de Marta es: {sueldo_Marta}")


sueldo_Erick = ( sueldo_base + bono2)
print(f"El sueldo de Erick es: {sueldo_Erick:.0f}")


sueldo_Cristian =( sueldo_base + bono3)
print(f"El sueldo de Cristian es: {sueldo_Cristian:.0f}")
