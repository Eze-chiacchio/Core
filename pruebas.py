import trio as t
#d = {2,5,6,7,7}
#print(id(d))
#print(type(d))
#j = {2,5,6,7,7}
#print(id({2,5,6,7,7}))
#print(type(d))
#print(d is j)

#try:
#    raise ZeroDivisionError("carlos")
#    raise SyntaxError
#except Exception as e:
#    print(e)
#while True == True:
#    pass

p = "flauta"
#d = "pirueta"
#print(f"toca la {p} y hace una {d}")

#match p:
#    case "flauta":
#        print("carlos")
#    case "pirueta":
#        print("marcelo")
#    case _:
#        print("ninguno")


#def funcion (valor1,valor2,*args,**kwargs):
#    print(type(args),type(kwargs))
#
#funcion(1,2,3,4,5,a=7,d=8)

def intdiv(a, b):
    try:
        result = a // b
        print("marcelo")
    except TypeError:
        print(	"Check operands. Some of them seems strange..."	)
    except ZeroDivisionError:
        print(	"Please do not divide by zero..."	)
    except Exception:
        print(	"Ups. Something went wrong..."	)

#intdiv(2,1)
#for elemento in map(lambda x: x *2,[1,2,3,4,5]):
#            print(elemento)

#lista = [1,2,3]
#lista2 = [1,2,3]
#lista = list(lista)
#lista2 = list(lista2)
#print(lista==lista2)
#print(lista is lista2)

#string = "string"
#string= string.split()
#
#__string = string
#print(__string)
#

#async def mycoro(*args, **kwargs):
# # … logic
# await t.run()
# # … more of our logic

def funcion(var1,var2):
    assert var1 >0,f"Error with {var1}"
try:
    print(funcion(-12,1))
except AssertionError as a:
    print(a)