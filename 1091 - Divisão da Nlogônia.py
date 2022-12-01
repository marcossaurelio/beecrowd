n = int(input())
i = 0

while n!=0:
    a,b = map(int, input().split(' '))
    while n>i:
        if n==0:
            break
        else:
            x,y = map(int, input().split(' '))
            if x==a or y==b:
                print("divisa")
            elif x>a and y>b:
                print("NE")
            elif x<a and y<b:
                print("SO")
            elif x<a and y>b:
                print("NO")
            elif x>a and y<b:
                print("SE")
            i += 1
    n = int(input())
    i = 0