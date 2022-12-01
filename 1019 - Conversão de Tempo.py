n = int(input()) #numero em segundos

h = n//3600 #3600 segundos == 1 hora
restoH = n%3600

m = restoH//60 #60 segundos == 1 minuto
restoM = restoH%60

s = restoM

print(f"{h}:{m}:{s}")