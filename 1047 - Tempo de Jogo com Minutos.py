# -*- coding: utf-8 -*-
hi,mi,hf,mf = input().split(' ')

hi = int((int(hi)**2)**0.5)
mi = int((int(mi)**2)**0.5)
hf = int((int(hf)**2)**0.5)
mf = int((int(mf)**2)**0.5)

hi = hi*60
hf = hf*60

if(hf+mf>hi+mi):
  print(f"O JOGO DUROU {(hf-hi+mf-mi)//60} HORA(S) E {(hf-hi+mf-mi)%60} MINUTO(S)")
else:
  print(f"O JOGO DUROU {(24*60-hi+hf-mi+mf)//60} HORA(S) E {(24*60-hi+hf-mi+mf)%60} MINUTO(S)")