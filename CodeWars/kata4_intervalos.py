#Intervals are represented by a pair of integers in the form of an array.
#The first value of the interval will always be less than the second value.
#Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

#[(1, 5), (6, 10)]
def sum_of_intervals(intervals):
    numeros = set()    
    for elemento in intervals:
        i = elemento[0]
        while i < elemento[1]:
            i += 1
            numeros.add(i)
    return len(numeros)

print(sum_of_intervals([(1, 5), (6, 10)]))