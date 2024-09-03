def somar (a, b):
    return a + b # me retorna o valor que foi calculado na minha função

print (f' a soma dos valores : {somar(4.7 ,7.7)}')  #chama o subprograma o nome da função e ()

def fatorial (n): #consigo chamar minha função dentro dela mesma >>>função recursiva<<<
    if n == 0:
        return 1
    else: 
        return n * fatorial (n-1)

print (f'numero fatorial: {fatorial (5)}')    