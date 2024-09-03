frutas = ['maça', 'banana', 'uva']  #lista
pessoa = {'nome': 'manu', 'idade': 18} #dicionário
numeros = [1,2,3,4,5,6,7,8,9,10] 
contador = 0 #variável pro contador

for chave, valor in pessoa.items(): #percorre dicionário com a chave e o valor
    print(f'Chave: {chave}, Valor: {valor}')

for fruta in frutas: #for intera listas, strings...
    print(f'frutas: {fruta}')

for x in range(1,10): #range percorre números, sempre até um antes do último
    print(x)

print('divisao pro terminal n ficar esquisito')

for numero in numeros: #continua nos pares e exibe os ímpares e quebraria no que eu der break
    if numero % 2 == 0:
        continue
    if numero == 9:
        break
    print(numero)

while (contador <=5):
    print(f'contador: {contador}')
    contador +=1