i = 0
positives = 0


while i<6:
    x = float(input())
    if x>0:
        positives += 1
    i += 1
    
print(f"{positives} valores positivos")