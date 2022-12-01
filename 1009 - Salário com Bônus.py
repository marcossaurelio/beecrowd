nome = str(input())
salarioFixo = float(input())
vendas = float(input())
comissao = float(15)/100
total = float(salarioFixo+(vendas*comissao))

print(f"TOTAL = R$ {total:.2f}")