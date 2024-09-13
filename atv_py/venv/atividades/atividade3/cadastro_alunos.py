class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def media_aluno (self):
        return(self.__nota1 + self.__nota2) / 2 
    
    def aluno_novo (nome, nota1, nota2):
        aluno_novo = Aluno (nome, nota1, nota2)
        cadastro_aluno.append(aluno_novo)

    def ler_dados ():
        nome = (input('Qual seu nome? '))
        nota1 = float(input ('Qual sua primeira nota? '))
        nota2 = float(input ('Qual a sua segunda nota? '))
        return nome, nota1, nota2
    
    def exibir_info (self):
        media = self.media_aluno()
        print(f'Seu nome é: {self.nome} e sua média é: {media: .2f}')

    nome, nota1, nota2 = ler_dados()
    aluno_novo(nome, nota1, nota2)


