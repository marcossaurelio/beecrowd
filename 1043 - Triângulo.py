from statistics import median

#area = (B + b).h/2

a,b,c = input().split(' ')

a = (float(a)**2)**0.5
b = (float(b)**2)**0.5
c = (float(c)**2)**0.5

if (min(a,b,c)+median([a,b,c])>max(a,b,c)):
  print(f"Perimetro = {a+b+c:.1f}")
elif (a!=0 and b!=0 and c!=0):
  print(f"Area = {((a+b)*c)/2:.1f}")