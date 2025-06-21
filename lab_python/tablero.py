#generar tablero de ajedres con movimiento mostrando el estado del tablero y registrando  captura de piesas

#crea diccionario(clave "coordenada" valor = " ")
tablero = {
    "a1": "TorreB", #fila 1
    "b1" :"CaballoB",
    "c1":"AlfilB", 
    "d1": "ReinaB", 
    "e1":"ReyB",
    "f1":"AlfilB",
    "g1":"CaballoB",
    "h1":"TorreB",
    # fila 2
    **{f"{columna}2":"PeonB" for columna in "abcdefgh"},

    # fila 7
    **{f"{columna}7":"PeonN" for columna in "abcdefgh"},

    # fila 8 
    "a8": "TorreN",
    "b8":"CaballoN",
    "c8":"AlfilN", 
    "d8":"ReinaN", 
    "e8":"ReyN",
    "f8":"AlfilN",
    "g8":"CaballoN",
    "h8":"TorreN",
}
# prepara dic con mapa de simbolos  pieza =>caracter

simbolos = {
    # blancas
    "TorreB":"R",
    "CaballoB":"N",
    "AlfilB":"B",
    "ReinaB":"Q",
    "ReyB":"K",
    "PeonB":"P",

    # negras
    "TorreN":"r",
    "CaballoN":"n",
    "AlfilN":"b",
    "ReinaN":"q",
    "ReyN":"k",
    "PeonN":"p"
}

    # mostrar tablero | por cada turno se imperima el tablero
def mostrar_tablero(tablero):
    print(" a b c d e f g h")
    for fila in range (8,0,-1):
        filastr = f"{fila}"
        for col in "abcdefgh":
            clave = f"{col}{fila}"
            pieza = tablero.get(clave,".")
            simbolo = simbolos.get(pieza,".")
            filastr += simbolo + " "
        print(filastr)


mostrar_tablero(tablero)