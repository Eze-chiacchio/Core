strr = "juan arlos pontevedra"
str2= "The quick brown fox jumps over the lazy dog"

###solucion 1
letras= {"a":0,
         "b":0,
         "c":0,
         "d":0,
         "e":0,
         "f":0,
         "g":0,
         "h":0,
         "i":0,
         "j":0,
         "k":0,
         "l":0,
         "m":0,
         "n":0,
         "o":0,
         "p":0,
         "q":0,
         "r":0,
         "s":0,
         "t":0,
         "u":0,
         "v":0,
         "x":0,
         "y":0,
         "z":0
         }

for elemento in str2:
    elemento= elemento.lower()
    if letras.get(elemento,None) != None:
        letras[elemento]+=1
if 0 in letras.values(): 
    print(False )
else:
    print(True)

#solucion 2 
s="juan carlos"
s = s.lower()
for char in 'abcdefghijklmnopqrstuvwxyz':
    if char not in s:
        print(False)
print(True)
