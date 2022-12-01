codigo, quantidade = input().split(" ")

quantidade = int(quantidade)
valorUnitario = 0

if(codigo == "1"):
  valorUnitario = float(4)
elif(codigo == "2"):
  valorUnitario = float(4.5)
elif(codigo == "3"):
  valorUnitario = float(5)
elif(codigo == "4"):
  valorUnitario = float(2)
elif(codigo == "5"):
  valorUnitario = float(1.5)

print(f"Total: R$ {(quantidade*valorUnitario):.2f}")