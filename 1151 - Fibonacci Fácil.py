n = int(input())
while n>=46 or n<=0:
    n = int(input())

x = 0
y = 0
i = 1

while i<n:
    if x==0 and y==0:
        y = 1
        print(f"{x}", end=" ")
        i += 1
    else:
        x = x+y
        y = x-y
        print(f"{x}", end=" ")
        i += 1

x = x+y
y = x-y
print(f"{x}")
i += 1