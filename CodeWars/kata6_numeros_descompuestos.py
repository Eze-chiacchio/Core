"""You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
"""

def expanded_form(num):
    solucion = []
    numeros = [int(a) for a in str(num)]
    cantidad_digitos = len(numeros) - 1
    for elemento in numeros:
        if elemento != 0:
            solucion.append(str(elemento) + str(0)*cantidad_digitos)
        cantidad_digitos-= 1
    return " + ".join(solucion)
print(expanded_form(215))