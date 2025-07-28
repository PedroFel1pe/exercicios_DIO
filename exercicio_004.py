#Crie uma superclasse Animal com o método falar(). Crie classes Vaca, Pato, Gato e Cachorro, cada uma sobrescrevendo falar().
# Crie uma lista com 1 objeto de cada tipo e use um for para chamar falar().

class Animal:
    def falar(self):
        raise NotImplementedError("As subclasses devem implementar este método") 
# raise = usar quando um método possa dar erro intencionalmente, dessa forma o código prosegue

class Vaca(Animal):
    def falar(self):
        print("A vaca faz MUUUUUUU")

class Pato(Animal):
    def falar(self):
        print("O pato QUA QUA")

class Gato(Animal):
    def falar(self):
        print("O gato MIAAAAAAAAUU")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro AU AU")

for animal in [Vaca(), Pato(), Gato(), Cachorro()]:
    animal.falar()