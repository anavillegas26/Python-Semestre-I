def dividir_numeros():
    try:         #solicitab dos numeros al usuario
        nun1 = float(input("Ingresa el primer numero:"))
        num2 = float(input("Ingrsa el segundo numero:"))
    
    #intentar la division
        resultado = nun1 / num2
        print(f"El resultado de la división es: {resultado:.2f}")
    except ValueError:
        print("¡Error! debes ingresar números válidos.") 
    except ZeroDivisionError:
        print("¡Error! no se puede dividir entre 0") 
    except Exception as e:
        print("Ocurrio un Error inesperado:{e}")
    finally:
        print("Fin del Programa.") 
# llamar funcion 
dividir_numeros()