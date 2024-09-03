nome = input('informe seu nome')
idade = int(input('informe sua idade')) #precisou do int pra o código não comparar string (idade) com inteiro (18)

if idade >=18:
    print(f'maior de idade {idade}')
else:
    print(f'menor de idade{idade}')