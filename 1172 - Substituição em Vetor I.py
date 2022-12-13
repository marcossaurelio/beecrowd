x = [None]*10
i = 0

while i<len(x):
    x[i] = int(input())
    i += 1
    
i = 0

while i<len(x):
    if x[i] <= 0:
        x[i] = 1
    i += 1
    
i = 0

while i<len(x):
    print(f'X[{i}] = {x[i]}')
    i += 1