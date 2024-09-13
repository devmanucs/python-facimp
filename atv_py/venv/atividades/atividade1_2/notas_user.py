soma = 0
qtd_notas = 0 
contador = 0

qtd_notas = int(input('Quantas notas deseja inserir? '))

while contador < qtd_notas:
    nota = float(input(f'Digite a nota {contador + 1}: '))
    soma += nota
    contador += 1

media = soma / qtd_notas

print(f'A media de notas é de {media: .2f}')
