a = 0
g = 0
d = 0
x = 0 #entrada do usuário

while x != 4:
    x = int(input())
    while x<1 or x>4:
        x = int(input())
    if x==1:
        a += 1
    elif x==2:
        g += 1
    elif x==3:
        d += 1
        
print("MUITO OBRIGADO")    
print(f"Alcool: {a}")
print(f"Gasolina: {g}")
print(f"Diesel: {d}")