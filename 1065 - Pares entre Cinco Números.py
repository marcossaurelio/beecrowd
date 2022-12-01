i = 0
pares = 0

while i<5:
    x = int(input())
    if x%2==0:
        pares += 1
    i += 1
    
print(f"{pares} valores pares")