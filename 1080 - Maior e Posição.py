i = 0
x = 0
maior = 0
posicao = 0

while i<100:
    x = int(input())
    while x<0:
        x = int(input())
    if x>maior:
        maior = x
        posicao = i+1
    i += 1
    
print(maior)
print(posicao)