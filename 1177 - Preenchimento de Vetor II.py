n = [None]*1000
i = 0
x = int(input())
j = 0

while j<1000:
    while i<x:
        n[j] = i
        j += 1
        i += 1
        if j>=len(n):
            break
    i = 0

k = 0
while k<len(n):
    print(f'N[{k}] = {n[k]}')
    k += 1