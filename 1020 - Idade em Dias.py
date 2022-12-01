n = int(input())

a = n//365
restoA = n%365

m = restoA//30
restoM = restoA%30

d = restoM

#saída
print(f"{a} ano(s)")
print(f"{m} mes(es)")
print(f"{d} dia(s)")