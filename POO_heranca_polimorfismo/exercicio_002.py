#Crie uma classe Funcionario com o método calcular_pagamento(). Crie duas classes que herdam:
# FuncionarioCLT: calcula salário fixo   FuncionarioPJ: calcula por hora
# Use um for para percorrer uma lista com ambos os tipos e imprimir calcular_pagamento().

class Funcionario:
    def __init__(self, nome, contrato):
        self.nome = nome
        self.contrato = contrato
    def calcular_pagamento(self):
        pass

class FuncionarioCLT(Funcionario):
    def calcular_pagamento(self):
        print(f"nome:{self.nome}, tipo de contrato: {self.contrato}")
        print("salario base: 1500R$, VR: 300R$, VT:150, total: 1950R$")

class FuncionarioPJ(Funcionario):
    def calcular_pagamento(self):
        print(f"nome:{self.nome}, tipo de contrato: {self.contrato}")
        print("salario por hora: 20R$, horas trabalhadas: 150, total: 3000R$")

for funcionario in [FuncionarioCLT("joão","CLT"), FuncionarioPJ("adriano", "PJ")]:
    funcionario.calcular_pagamento()