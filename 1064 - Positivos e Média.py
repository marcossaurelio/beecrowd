i = 0
positives = 0
xs = 0
xi = 0

while i<6:
    x = float(input())
    if x>0:
        positives += 1
        xs += x
        xi += 1
    i += 1
    
print(f"{positives} valores positivos")
print(f"{(xs/xi):.1f}")