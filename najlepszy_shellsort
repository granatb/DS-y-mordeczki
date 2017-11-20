def shell_sort(t):
    n = len(t)
    h = 1
    while True:
        h = 3*h + 1
        if h >= n:
            h = h//9
            break
    if h == 0:
        h = 1
    while h >0:
        for j in range(n-h-1,-1,-1):
            x = t[j]
            i = j+h
            while i <= n-1 and x > t[i]:
                t[i-h] = t[i]
                i = i+h
            t[i-h] = x
        h = h//3
    return t

import random
n = int(input("podaj dlugosc listy t"))
t = [random.randint(0,10000) for i in range(n)]

print(shell_sort(t))
