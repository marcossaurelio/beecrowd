n = int(input())
i = 0
x = 0
dentro = 0
fora = 0

while i<n:
    x = int(input())
    if x>=10 and x<=20:
        dentro += 1
    else:
        fora += 1
    i += 1

print(f"{dentro} in")
print(f"{fora} out")