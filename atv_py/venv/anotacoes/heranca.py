class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        ... #define que o método não tem nenhum comportamento
class Cachorro(Animal):
    def falar (self):
        return f'{self.nome} late!'
    
class Gato(Animal):
    def falar(self):
        return f' {self.nome} mia!' 

bolinha = Cachorro('bolinha')
bartô = Gato('bartô')

print(bolinha.falar())
print(bartô.falar())