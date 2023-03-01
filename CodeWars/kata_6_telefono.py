from dis import pretty_flags


numeros = [1,2,3,4,5,6,7,8,9,0]

###solucion1
prefijo= [str(x) for i,x in enumerate(numeros) if i<3]
segmento1 = [str(x) for i,x in enumerate(numeros) if i in (3,4,5)]
segmento2 = [str(x) for i,x in enumerate(numeros) if i>5]
print("(" + "".join(prefijo) + ")" + " " + "".join(segmento1) + "-" + "".join(segmento2))

###solucion2
print("({}{}{}) {}{}{}-{}{}{}{}".format(*numeros))
