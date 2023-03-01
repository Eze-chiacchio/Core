strr = 'abba'
words = ['aabb', 'abcd', 'bbaa', 'dada']
#solucion 1
def anagrams(word, words):
    strr = sorted(word)
    anagramas = []
    for elemento in words:
        if sorted(elemento) == strr:
            anagramas.append(elemento)
    return anagramas

#solucion 2

def anagrams(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]
