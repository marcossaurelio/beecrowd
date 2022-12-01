x = int(input())
i = 1

while x<1 or x>1000:
    x = int(input())
    
while i%2==1 and i<=x:
    print(i)
    i+=2