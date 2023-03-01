""" The goal of this exercise is to convert a string to a new string where each character
    in the new string is "(" if that character appears only once in the original string,
    or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
"""
#primer solucion
def duplicate_encode(word):
    letras,salida= {},[]
    for elemento in word:
        elemento = elemento.lower()
        if letras.get(elemento,None) != None:
            letras[elemento] = letras[elemento] + 1
        else:
            letras[elemento] = 1
    for elemento in word:
        elemento = elemento.lower()
        if letras.get(elemento) == 1:
            salida.append('(')
        else:
            salida.append(')')
    return "".join(salida)
print(duplicate_encode("dind"))

#segunda solucion
def duplicate_encode(word):
    letras = ["(" if word.lower().count(c) == 1 else ")" for c in word.lower()]
    return "".join(letras)
