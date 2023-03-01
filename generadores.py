def numeros_naturales():
    n=1
    for _ in range(6): 
        yield n
        n += 1

def lista():
    lista=[1,3,5,7,9]
    for elemento in lista:
        yield elemento

#for natural in numeros_naturales():
#    print(natural)

a = numeros_naturales()

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

#for elemento in lista():
#    print(elemento)