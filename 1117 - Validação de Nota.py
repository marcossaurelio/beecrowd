nota1 = float(input())
while nota1<0 or nota1>10:
    print("nota invalida")
    nota1 = float(input())

nota2 = float(input())
while nota2<0 or nota2>10:
    print("nota invalida")
    nota2 = float(input())
    
print(f"media = {(nota1+nota2)/2}")