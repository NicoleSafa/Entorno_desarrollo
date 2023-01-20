
"""
Escribe un programa que almacene las asignaturas de un curso (por ejemplo
Informática, Francés, Filosofía, Ética y Álgebra) en una lista y la muestre por pantalla el
mensaje “Yo estudio <asignatura>”, donde “asignatura” es cada una de las asignaturas
de la lista
"""

#defino primero la lista de las asignaturas
list_asignaturas= ("Informatica", "Frances", "Filosofia", "Etica", "Algebra")

#uso el for para recorrer mi lista asignatura por asignatura
for asignaturas in list_asignaturas:
    print("Yo estudio " + asignaturas)
