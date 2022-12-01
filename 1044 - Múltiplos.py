a,b = input().split(" ")

a = int(a)
b = int(b)

if(a!=0 and b!=0):
  if(max(a,b)%min(a,b)==0):
    print("Sao Multiplos")
  else:
    print("Nao sao Multiplos")
else:
  print("Nao sao Multiplos")