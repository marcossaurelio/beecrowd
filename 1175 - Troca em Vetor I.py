n = [None]*20
i = 0

while i<len(n):
    n[i] = int(input())
    i += 1

i = 0

while i<len(n)//2:
    aux = n[i]
    n[i] = n[len(n)-1-i]
    n[len(n)-1-i] = aux
    i += 1
    
i = 0

while i<len(n):
    print(f'N[{i}] = {n[i]}')
    i += 1