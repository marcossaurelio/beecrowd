calcula_media = 1

while calcula_media==1:
    nota1 = float(input())
    while nota1<0 or nota1>10:
        print("nota invalida")
        nota1 = float(input())

    nota2 = float(input())
    while nota2<0 or nota2>10:
        print("nota invalida")
        nota2 = float(input())

    print(f"media = {(nota1+nota2)/2:.2f}")
    
    print("novo calculo (1-sim 2-nao)")
    calcula_media = int(input())
    while calcula_media!=1 and calcula_media!=2:
        print("novo calculo (1-sim 2-nao)")
        calcula_media = int(input())