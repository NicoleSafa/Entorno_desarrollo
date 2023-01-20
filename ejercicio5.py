"""
El programa debe preguntar al usuario por una frase y una letra, y mostrar por
pantalla el número de veces que aparece la letra en la frase.
"""

frase= input("Introduce una frase porfa")
letra= input("Introduce una letra porfa")

contador= 0

for i in frase:
    if i == letra:
        contador +=1
print("La letra "+ letra + " aparece " + str(contador) + " veces en la frase.")



