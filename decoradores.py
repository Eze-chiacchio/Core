def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

print(suma(3,2))

'''Lo que realiza mi_decorador() es definir una nueva función que encapsula o envuelve la función que se pasa como entrada. 
Concretamente lo que hace es hace uso de dos print(), uno antes y otro después de la llamada la función.

Por lo tanto, cualquier función que use @mi_decorador tendrá dos print, uno y al principio y otro al final, 
dando igual lo que realmente haga la función.'''