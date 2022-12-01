consumo = 12 #km/l
tempo = int(input())
velocidade = int(input())
distancia = tempo*velocidade
litros = float(distancia/consumo)

print(f"{litros:.3f}")