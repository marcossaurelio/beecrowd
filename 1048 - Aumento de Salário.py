salario = float(input())

if(salario>=0 and salario<=400):
  reajuste = 0.15
  print(f"Novo salario: {salario*(1+reajuste):.2f}")
  print(f"Reajuste ganho: {salario*reajuste:.2f}")
  print(f"Em percentual: {int(reajuste*100)} %")
if(salario>400 and salario<=800):
  reajuste = 0.12
  print(f"Novo salario: {salario*(1+reajuste):.2f}")
  print(f"Reajuste ganho: {salario*reajuste:.2f}")
  print(f"Em percentual: {int(reajuste*100)} %")
if(salario>800 and salario<=1200):
  reajuste = 0.10
  print(f"Novo salario: {salario*(1+reajuste):.2f}")
  print(f"Reajuste ganho: {salario*reajuste:.2f}")
  print(f"Em percentual: {int(reajuste*100)} %")
if(salario>1200 and salario<=2000):
  reajuste = 0.07
  print(f"Novo salario: {salario*(1+reajuste):.2f}")
  print(f"Reajuste ganho: {salario*reajuste:.2f}")
  print(f"Em percentual: {int(reajuste*100)} %")
if(salario>2000):
  reajuste = 0.04
  print(f"Novo salario: {salario*(1+reajuste):.2f}")
  print(f"Reajuste ganho: {salario*reajuste:.2f}")
  print(f"Em percentual: {int(reajuste*100)} %")