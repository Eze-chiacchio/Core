from coreapi import Object


resultado =((lambda x: x*2) (10))
print(resultado )

lista = [1,2,3,4]

# Example of lambda function using if-else
Max = lambda a, b : a if(a > b) else b

print(Max(1, 2))

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtrado = filter(lambda x: x % 2 != 0, mi_lista)

list(filtrado)
class Objeto:
    def __init__(self,fecha):
        self.fecha = fecha
lista2 = [Objeto(20211212),
Objeto(20210720),
Objeto(20220220),
Objeto(20210920),]

def ordenar_lista_objetos(lista2):
    lista = [item for item in lista2]
    lista.sort(key = lambda x:x.fecha)
    print (lista[-1].fecha)
ordenar_lista_objetos(lista2)