"""
El programa debe recibir una cadena de caracteres y devolver un diccionario
con cada palabra que contiene y el número de veces que aparece.
Otra función que reciba el diccionario generado con la función anterior y
devuelva una tupla con la palabra más repetida y su frecuencia.
"""

def contador_palabras(texto):

    texto_dividido= texto.split()
    palabras= {}

    for variable in texto_dividido:
        if variable in palabras:
            palabras[variable] += 1
        else:
            palabras[variable] = 1
    return palabras

#devolver palabra que mas aparece
def mas_repetido(palabras):

    max_palabra= ''
    max_freq= 0

    for palabra, freq in palabras.items():
        if freq > max_freq:
            max_palabra = palabra
            max_freq = freq
    return max_palabra, max_freq

texto = "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"
print(contador_palabras(texto))
print(mas_repetido(contador_palabras(texto)))