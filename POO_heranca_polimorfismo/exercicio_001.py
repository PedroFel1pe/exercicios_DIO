#Crie uma classe Veiculo com atributos marca e modelo e um método ligar(). Depois crie duas classes filhas:
# Carro (com método abrir_porta())     Moto (com método subir_na_moto())

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def ligar(self):
        print(f"Ligando o motor do(a) {self.modelo}")
        print("Motor ligado")

class Carro(Veiculo):
    def abrir_porta(self):
        print("Porta aberta...entrando no carro...fechando porta")

class Moto(Veiculo):
    def subir_na_moto(self):
        print("Montado na moto")

tipo = input("Informe o tipo de seu veiculo(carro ou moto): ").lower().strip()
marca = input("informe a marca do seu veiculo: ").upper().strip()
modelo = input("informe agora o modelo: ").lower().strip()

if tipo == "carro":
    veiculo = Carro(marca, modelo)
    veiculo.abrir_porta()
elif tipo == "moto":
    veiculo = Moto(marca, modelo)
    veiculo.subir_na_moto()
else:
    print("tipo de veiculo não correspondente")

veiculo.ligar()