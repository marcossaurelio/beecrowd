n = [None]*10
v = int(input())
i = 0

while i<len(n):
    n[i] = v
    v *= 2
    i += 1
    
i = 0
    
while i<len(n):
    print(f'N[{i}] = {n[i]}')
    i += 1