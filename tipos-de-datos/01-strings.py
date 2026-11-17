"""Escribe una función que reciba una cadena de texto como parámetro y 
devuelva un diccionario con las frecuencias de cada letra en la cadena.
Los espacios no deben ser considerados."""

def conversor(cadena):
    diccionario = {}
    cadenaModificada = cadena.replace(" ", "")
    contador = 1;
    for caracter in cadenaModificada:
        diccionario[contador] = caracter
        contador += 1
    return diccionario

print(conversor("ejercicio 1"))