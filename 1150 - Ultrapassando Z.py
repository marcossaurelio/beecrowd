x = int(input())
y = int(input())
while x>=y:
    y = int(input())

s = 0
i = 0

while s<=y:
    i += 1
    s += x
    x += 1

print(i)