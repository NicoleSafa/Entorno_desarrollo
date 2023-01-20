
"""
El programa debe convertir un número decimal en binario. Otra función,
convertirá un número binario en decimal.
El siguiente código es cercano a la solución, pero contiene errores. Haciendo
uso del debugger, explica cómo has encontrado la solución y cuál es esta
"""

def a_decimal(n):

    n= list(n)
    n.reverse()
    decimal= 0

    for i in range(len(n)):
        decimal= int(n[int(i)]) * 2 ** int(i)
    return decimal

def a_binario(n):
    binario= []

    while n> 0:
        binario.append(str(n%2))
        n //= 2
    binario.reverse()
    return ''.join(binario)

print(a_decimal("10110"))
print(a_binario(22))

print(a_decimal(a_binario(22)))
print(a_binario(a_decimal("10110")))
