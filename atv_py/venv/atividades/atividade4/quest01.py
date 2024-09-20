#exercício de sala 13/09/2024. Instruções:​ Crie uma classe base chamada "Empregado" que contenha atributos gerais como nome e salario_base. ​Crie subclasses como "Gerente" e "Vendedor", que herdam de "Empregado", com suas próprias regras de cálculo de salário (por exemplo, o gerente tem um bônus fixo, enquanto o vendedor tem uma comissão sob as vendas).

class Empregado:
    def _init_(self, nome, salario_base:float):
        self.nome = nome
        self.salario_base = salario_base

    def valores(self):
        ...

class Gerente(Empregado):
    def valores(self):
       # self.bonus_fixo = bonus_fixo
       # self.renda_mensal = renda_mensal
        return f'{self.nome} recebe: {self.salario_base + (self.salario_base*0.10)}'
    
class Vendedor(Empregado):
    def valores(self):
        return f'{self.nome} recebe: {self.salario_base + (self.salario_base*0.02)}'

barto = Gerente('Bartolomeu Nagano', 3000, 100)
print(barto.valores())
cj = Vendedor('Christopher Jonny', 1500,0.5,1000)
print(cj.valores())






    

        
       