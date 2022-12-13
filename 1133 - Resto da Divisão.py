x = -1
y = -1

while x<=0:
    x = int(input())
while y<=0:
    y = int(input())

menor = min(x,y) + 1
maior = max(x,y)

while menor<maior:
    if menor%5==2 or menor%5==3:
        print(menor)
    menor += 1