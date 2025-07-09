#crear diccionario
tiempo = {
    5700000:{"ciudad":"Castro", "Temperatura":11.8,"Precipitación":2000} ,
    5770000:{"ciudad": "Chonchi", "Temperatura":8.3, "Precipitación":2800},
    5790000:{"ciudad":"Quellón", "Temperatura":10.2, "Precipitación":2959}
}
print(tiempo)

temperatura_Castro = 11.8

if temperatura_Castro > 10 :
   print("La temperatuta es Frio")
elif temperatura_Castro > 15:
   print("la temperatura es templado")

else:
   print("la temperatura es calida")
print(temperatura_Castro)

#agregar la clave clima

temperatura_Chonchi= 8.3

if temperatura_Chonchi > 10 :
   print("La temperatuta es Frio")
elif temperatura_Chonchi> 15:
   print("la temperatura es templado")

else:
   print("la temperatura es calida")
print(temperatura_Chonchi)


temperatura_Quellón= 10.2

if temperatura_Quellón > 10 :
   print("La temperatuta es Frio")
elif temperatura_Quellón> 15:
   print("la temperatura es templado")

else:
   print("la temperatura es calida")
print(temperatura_Quellón)

#agregar la clave clima
tiempo [5700000]["clima"] ="frio"
tiempo[5770000]["clima"] = "calido"
tiempo[5790000]["clima"]="frio"

print(tiempo)

tiempo[5700000]["meses_mas_lluviosos"]= list()
print(tiempo)

tiempo[5700000]["meses mas lluviosos"]= list("mayo,junio,julio")
tiempo[5770000]["meses mas lluviosos"]= list("mayo,junio,julio")
tiempo[5790000]["meses mas lluviosos"]= list("mayo,junio,julio")
print(tiempo)
print(tiempo)

