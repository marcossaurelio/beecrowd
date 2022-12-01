n1,n2,n3,n4 = input().split(' ')

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1*2+n2*3+n3*4+n4*1)/(2+3+4+1)

print(f"Media: {media:.1f}")

if (media >= 7):
    print("Aluno aprovado.")
if (media < 5):
    print("Aluno reprovado.")
if (5 <= media < 7):
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media = (media+nota_exame)/2
    if (media >=5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")