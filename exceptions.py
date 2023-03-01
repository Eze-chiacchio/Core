def lanzador():
    raise Exception


try:
    raise FileNotFoundError
    raise SyntaxError
    print("ejecucion")
except ZeroDivisionError as e:
    print("custom")
except SyntaxError as ex:
    print("base")
