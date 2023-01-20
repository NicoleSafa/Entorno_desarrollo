""""
Escribir un programa que almacene la cadena de caracteres 12345EDD como
contraseña. En una variable, pregunte al usuario por la contraseña hasta que
introduzca la contraseña correcta.
"""

contrasenia= "12345EDD"

respuesta= input("Cual crees que es la contrasenia?")

while respuesta != contrasenia:
    print("Sigue intentando")
    respuesta= input("Cual crees que es la contrasenia?")
if (respuesta == "12345EDD"):
    print("La has adivinado!")