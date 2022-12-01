valor = int(input())

#Saída de Notas, nomes das variáveis são o valor de cada nota em algarismos romanos para facilitar a escrita do algoritmo.
#Primeiro se calcula a quantidade de notas de cada valor que irá sair e depois se calcula o resto que sobra da operação, em ordem decrescente e repetidamente até a nota de 1 real.

c = int(valor//100)
restoC = int(valor%100)

l = int(restoC//50)
restoL = int(restoC%50)

xx = int(restoL//20)
restoXx = int(restoL%20)

x = int(restoXx//10)
restoX = int(restoXx%10)

v = int(restoX//5)
restoV = int(restoX%5)

ii = int(restoV//2)
restoIi = int(restoV%2)

i = int(restoIi//1)

print(valor)
print(f"{c} nota(s) de R$ 100,00")
print(f"{l} nota(s) de R$ 50,00")
print(f"{xx} nota(s) de R$ 20,00")
print(f"{x} nota(s) de R$ 10,00")
print(f"{v} nota(s) de R$ 5,00")
print(f"{ii} nota(s) de R$ 2,00")
print(f"{i} nota(s) de R$ 1,00")