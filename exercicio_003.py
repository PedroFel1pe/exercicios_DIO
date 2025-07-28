#Crie uma classe Pessoa com atributos nome e idade.Crie a classe Aluno, herdando Pessoa, e adicione matricula como novo atributo.
# Use super().__init__() para reaproveitar o construtor da classe mãe.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def cadastro(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
    def cadastro(self):
        return f"registro de cadastro: {self.matricula}, nome:{self.nome}, idade: {self.idade}"

aluno = Aluno("pedro", "27", "38")
print(aluno.cadastro())