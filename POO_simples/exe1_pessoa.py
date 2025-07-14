#Crie uma classe Pessoa com os atributos nome e idade. Inclua um método que diz se a pessoa é maior de idade (idade >= 18).
#vou praticar inglês tambem
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def isAdult(self):
        if self.age >= 18 :
            return f"{self.name} is of legal age at {self.age} years old."
        else:
            return f"{self.name} is minor at {self.age} years old."

name = str(input("What`s your name: "))
age = int(input("what`s your age: "))
person = Person(name, age)
conclusion = person.isAdult()
print(conclusion)
