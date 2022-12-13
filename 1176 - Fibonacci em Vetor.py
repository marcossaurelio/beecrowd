fib = [None]*61
fib[0] = 0
fib[1] = 1
i = 2

while i<len(fib):
    fib[i] = fib[i-2] + fib[i-1]
    i += 1

n = int(input())
i = 0

while i<n:
    x = int(input())
    print(f'Fib({x}) = {fib[x]}')
    i += 1