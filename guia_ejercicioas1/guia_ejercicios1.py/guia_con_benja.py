#ejercicio 3 , 3 vendedores registran sus ventas durante 5 días
sueldo_base = 529000

ventas_diarias = {
    "Marta" :[120000,80000,110000,80000,100000  ],
    "Cristian" : [300000,460000,330000,250000,200000 ],
    "Erick" : [220000,130000,280000,200000,400000]
}       
print(ventas_diarias) 

ventas_totales_E= ventas_diarias["Erick":[sum/5] ]
ventas_totales_C= ventas_diarias["Cristian"]
ventas_totales_M=ventas_diarias["Marta"]
print(ventas_totales_E)
print(ventas_totales_C)
print(ventas_totales_M)

#calcular el total de ventas de cada vendedor

try:
    if ventas_totales_M > 1500000:
        bono = sueldo_base * 0.20
    elif ventas_totales_M > 1000000:
        bono = sueldo_base * 0.10
    elif ventas_totales_M > 500000:
        bono = sueldo_base * 0.05
    else:
        bono = 0
        print (bono)
finally:
    print(f"Marta recibe: {bono}")

