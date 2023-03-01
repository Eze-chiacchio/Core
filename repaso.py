from pruebas import funcion


def decorador1(funcion):
    def funcionfuncion(e1,e2):
        print("se va  a llamar la funcion")
        resu = funcion(e1,e2)
        return resu
    return funcionfuncion

@decorador1
def funcion_nueva(elemento1,elemento2):
    return elemento1 + elemento2
print(funcion_nueva(12,6))
