
"""
El programa debe almacenar los vectores (1, 2, 3) y (-1, 0, 2) en dos listas y
muestre por pantalla su producto escalar.
"""

lista_a= (1, 2, 3)
lista_b= (-1, 0, 2)
producto= (0,)

for i in range(1):
    resultado= (lista_a[i-1]* lista_b[i-1])

    print("El producto de los vectores " + str(lista_a) + " y " + str(lista_b) + " es " + str(resultado))

