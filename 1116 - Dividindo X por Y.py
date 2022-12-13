n = int(input())
i = 0
x,y = 0,0

while i<n:
    x,y = map(int, input().split(' '))
    if y==0:
        print("divisao impossivel")
    else:
        print(f"{(x/y):.1f}")
    i += 1