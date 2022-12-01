from statistics import median

a,b,c = input().split(' ')

a = (float(a)**2)**0.5
b = (float(b)**2)**0.5
c = (float(c)**2)**0.5

aux_a = max(a,b,c)
aux_b = median([a,b,c])
aux_c = min(a,b,c)

a = aux_a
b = aux_b
c = aux_c

if(a>=b+c):
  print("NAO FORMA TRIANGULO")
else:
  if(a**2==b**2+c**2):
    print("TRIANGULO RETANGULO")
  if(a**2>b**2+c**2):
    print("TRIANGULO OBTUSANGULO")
  if(a**2<b**2+c**2):
    print("TRIANGULO ACUTANGULO")
  if(a==b and b==c):
    print("TRIANGULO EQUILATERO")
  if((a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)):
    print("TRIANGULO ISOSCELES")