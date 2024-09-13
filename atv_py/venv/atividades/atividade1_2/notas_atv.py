n1 = float(input('insira sua primeira nota: '))
n2 = float(input('insira sua segunda nota: '))
n3 = float(input('insira sua terceira nota: '))
n4 = float(input('insira sua quarta nota: '))
media = n1+n2+n3+n4 / 4
if media >= 7:
    print('aluno aprovado')
else:
    print('aluno reprovado')