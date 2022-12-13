a = [None]*100
i = 0

while i<len(a):
    a[i] = float(input())
    if a[i]<=10:
        print(f'A[{i}] = {a[i]:.1f}')
    i += 1