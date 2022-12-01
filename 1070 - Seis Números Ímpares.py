x = int(input())
i = 0

while x<=0:
    x = int(input())
    
while i<6:
    if x%2==0:
        x += 1
    print(x)
    x += 2
    i+=1