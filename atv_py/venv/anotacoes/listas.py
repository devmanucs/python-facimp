lista = [5,2,7,4] #lista
lista [3] = 10 #modifica um dos itens que tem dentro da minha lista
lista.append('manu') #adiciona um item na listinhawn
lista.remove(2) #remove pelo item no seco, em específico
del lista[0] #remove pelo índice, ou seja, o 1 vai de base

print(len(lista)) #descubro o tamanho da peste da lista, logo, meio inutil

for elemento in lista: #guarda tudo que tem dentro da minha lista na miseria da variável elemento 
    print(elemento) #vai exibir toda a minha lista pq esse pestezinha percorreu ela toda

if 3 in lista: #daqui
    print('o valor está na lista')
else :
    print('o valor não está na lista') # (até aqui) me indica se possuo um valor na lista

x = 5 #mesma coisa de cima só que com variável indicando o valor
if x in lista: 
    print(f'o valor {x} está na lista')
else:
      print(f'o valor {x} não está na lista')
      