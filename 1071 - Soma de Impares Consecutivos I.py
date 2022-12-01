x = int(input())
y = int(input())

min = min(x,y)+1
max = max(x,y)

soma = 0

while min<max:
    if min%2==0:
        min += 1
    soma += min
    min += 2
    
print(soma)