#primer solucion
def two_sum(numbers, target):
    resultado = []
    for i,elemento1 in enumerate(numbers):
        posicion = len(numbers)
        while posicion > 0:
            if numbers[posicion - 1] + elemento1 == target:
                resultado.append(posicion-1)
                resultado.append(i)
                return resultado
            posicion -=1
    return []
print(two_sum([1234,5678,9012], 14690))

#segunda solucion
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]