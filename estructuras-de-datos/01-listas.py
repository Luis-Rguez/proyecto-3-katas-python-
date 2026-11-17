"""3. Escribe una función que tome una lista de palabras y una palabra objetivo
 como parámetros. La función debe devolver una lista con todas las palabras de 
 la lista original que contengan la palabra objetivo."""

def buscarPalabra(lista, palabra):
    listaEncontrada = []
    for palabraLista in lista:
        if palabra == palabraLista:
            listaEncontrada.append(palabraLista)
    return listaEncontrada

listaPalabras = ["pelota", "raqueta", "red", "pelota", "banda", "pelota"]
palabraObjetivo = "pelota"

print(list(buscarPalabra(listaPalabras, palabraObjetivo)))
