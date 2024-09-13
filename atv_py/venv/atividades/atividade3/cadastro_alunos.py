class Aluno:
    def __init__(self, nome: str, nota1: float, nota2: float):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def get_nome (self):
        return self.__nome
    
    def get_nota1 (self):
        return self.__nota1
    
    def get_nota2 (self):
        return self.__nota2
    
    def get_media (self):
        return (self.__nota1 + self.__nota2) /2

def aluno_novo ():
    nome = input('Qual seu nome? ')
    nota1 = float(input('Qual sua primeira nota? '))
    nota2 = float(input('Qual sua segunda nota? '))
    return Aluno (nome, nota1, nota2)
    
Aluno = aluno_novo()
print (f'Nome: {Aluno. get_nome ()}')
print (f'Primeira nota : {Aluno. get_nota1 ()}')
print (f'Segunda nota : {Aluno. get_nota2 ()}')
print(f'A média é: {Aluno. get_media ()} ')

