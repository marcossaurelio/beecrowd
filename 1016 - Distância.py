velocidadeX = int(60)
velocidadeY = int(90)
distancia = int(input())
minutosParaDistancia = int((distancia)*float(60/(((velocidadeX-velocidadeY)**2)**(1/2))))

print(f"{minutosParaDistancia} minutos")