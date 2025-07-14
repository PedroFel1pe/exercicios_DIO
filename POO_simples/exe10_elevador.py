#Um pouco mais complexo: crie uma classe Elevador com:Atributos: andar atual, total de andares, capacidade, quantidade de pessoas.Métodos para entrar, sair, subir andar e descer andar. Faça validações para não ultrapassar capacidade e limites de andares.
class Elevador:
    def __init__(self, total_andar, andar_atual,peso_atual,quant_pessoas):
        self.total_andar = total_andar
        self.andar_atual = andar_atual
        self.peso_atual = peso_atual
        self.quant_pessoas = quant_pessoas
        #limites
        self.max_pessoas = 6
        self.max_peso = 500
    def entrar(self, pessoa, peso):
        self.quant_pessoas += pessoa
        self.peso_atual += peso
        if self.quant_pessoas > self.max_pessoas:
            return "Quantidade máxima de pessoas excedida"
        elif self.peso_atual > self.max_peso:
            return "Peso máximo excedido"
        else:
            return "Quantidade de pessoas e peso corretas"

    def sair(self):
        return "saindo do elevador, tchau =)"
    def subir_andar(self, caminho):
        if caminho > self.total_andar:
            return "andar inválido para subida"
        for i in range(self.andar_atual + 1, caminho + 1):
            print(f"subindo ...andar {i}")
        self.andar_atual = caminho
        return f"Você chegou ao andar {self.andar_atual}"     
    def descer_andar(self, caminho):
        if caminho < 0:
            return "Andar inválido para descida."
        for i in range(self.andar_atual - 1, caminho - 1, -1):
            print(f"Descendo... Andar {i}")
        self.andar_atual = caminho
        return f"Você chegou ao andar {self.andar_atual}"

elevador = Elevador(10, 8, 0, 0)
opcao = input("quer entrar ou sair: ").lower()
if opcao == "entrar":
    pessoa = int(input("quantas pessoas vão entrar: "))
    peso = float(input("qual o peso total delas: Kg "))
    print(elevador.entrar(pessoa, peso))
    if pessoa <= 6 and peso <= 500:
        caminho = int(input("que andar deseja ir de 1 a 10: "))
        if caminho > elevador.andar_atual:
            print(elevador.subir_andar(caminho))
        elif caminho < elevador.andar_atual:
            print(elevador.descer_andar(caminho))
        else:
            print("opção invalida")
    else:
        print("elevador bloqueado")
elif opcao == "sair":
    print(elevador.sair())
else:
    print("opção invalida")
