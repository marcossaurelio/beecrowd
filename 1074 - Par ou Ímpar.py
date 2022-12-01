n = int(input())
i = 0

while n>=10000:
    n = int(input())
    
while i<n:
    x = int(input())
    while x<=(-10**7) or x>=(10**7):
        x = int(input())
    if x==0:
        print("NULL")
    else:
        if x%2==0:
            print("EVEN", end=" ")
        if x%2!=0:
            print("ODD", end=" ")
        if x>0:
            print("POSITIVE")
        if x<0:
            print("NEGATIVE")
    i+=1