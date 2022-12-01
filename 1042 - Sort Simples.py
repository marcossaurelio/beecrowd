from statistics import median

a,b,c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

print(min(a,b,c))
print(median([a,b,c]))
print(max(a,b,c))

print()

print(a)
print(b)
print(c)