n = int(input())
i = 0
x = 0
idiv = 1
s = 0

while i<n:
    x = int(input())
    while idiv<=x:
        if x%idiv==0:
            s += 1
        idiv += 1
    if s==2:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
    s = 0
    idiv = 1
    i += 1