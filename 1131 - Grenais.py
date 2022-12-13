i = 1
wi = 0 #vitórias do inter
wg = 0 #vitórias do grêmio
d = 0 #empates

while i==1:
    inter,gremio = map(int, input().split(' '))
    if inter>gremio:
        wi += 1
    elif inter<gremio:
        wg += 1
    elif inter==gremio:
        d += 1
    print("Novo grenal (1-sim 2-nao)")
    i = int(input())
    
print(f"{wi+wg+d} grenais")
print(f"Inter:{wi}")
print(f"Gremio:{wg}")
print(f"Empates:{d}")
if wi>wg:
    print("Inter venceu mais")
elif wi<wg:
    print("Gremio venceu mais")
elif wi==wg:
    print("Nao houve vencedor")