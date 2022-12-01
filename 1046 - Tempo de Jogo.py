hi,hf = input().split(' ')

hi = int((int(hi)**2)**0.5)
hf = int((int(hf)**2)**0.5)

if(hf>hi):
  print(f"O JOGO DUROU {hf-hi} HORA(S)")
else:
  print(f"O JOGO DUROU {24-hi+hf} HORA(S)")