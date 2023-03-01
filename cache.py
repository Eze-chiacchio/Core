import time

def es_primo_concache(num, _cache={}):
    if num not in _cache:
        _cache[num] = True
        for n in range(2, num):
            if num % n == 0:
                _cache[num] = False
                break
    return _cache[num]

tic = time.time()
print(es_primo_concache(25565479))
print(time.time() - tic)

tic = time.time()
print(es_primo_concache(25565479))
print(time.time() - tic)
