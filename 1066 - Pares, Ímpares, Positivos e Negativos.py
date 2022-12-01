i = 0
pares = 0
impares = 0
pos = 0
neg = 0

while i<5:
    x = int(input())
    if x%2==0:
        pares += 1
    if x%2!=0:
        impares += 1
    if x>0:
        pos += 1
    if x<0:
        neg += 1
    i += 1
    
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")