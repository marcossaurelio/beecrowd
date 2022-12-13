o = input()

soma = 0
dimen = 12
m = []
for i in range(dimen):
    linha = []
    for j in range(dimen):
        x = float(input())
        if j > dimen-1-i:
            soma += x
        linha.append(x)
    m.append(linha)

if o == 'S' or o == 's':
    print(soma)
elif o == 'M' or o == 'm':
    print(f'{(soma/((len(m)-1)*(len(m)/2))):.1f}')