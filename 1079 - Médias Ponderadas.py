n = int(input())
i = 0

while i<n:
    x1,x2,x3 = input().split(' ')
    
    x1 = float(x1)
    x2 = float(x2)
    x3 = float(x3)
    
    print(f"{(x1*2+x2*3+x3*5)/(2+3+5):.1f}")
    
    i += 1