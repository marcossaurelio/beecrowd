i = 0
s = 0
x = int(input())

while x>0:
    i += 1
    s += x
    x = int(input())
    
print(f"{s/i:.2f}") #media