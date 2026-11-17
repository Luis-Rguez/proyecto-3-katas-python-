"""Dada una lista de números, obtén una nueva lista con el doble de cada valor.
Usa la función map()."""

lista = [1,4,8,5,6,3,5]

def listaDoble(lista):
    doble = map(lambda x: x*2, lista)
    return doble

print(lista)
print(list(listaDoble(lista)))