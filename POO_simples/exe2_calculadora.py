#Crie uma classe Calculadora que tenha métodos para somar, subtrair, multiplicar e dividir dois números. Faça métodos para cada operação e teste a classe com diferentes valores
#estou treinando inglês tambem =)
class calculator:
    def __init__(self, number1, number2, operator):
        self.number1 = number1
        self.number2 = number2
        self.operator = operator
    
    def sum(self):
        return self.number1 + self.number2
    def subtraction(self):
        return self.number1 - self.number2
    def multiplication(self):
        return self.number1 * self.number2
    def division(self):
        if self.number2 == 0:
            return "error: Division by zero"
        return self.number1 / self.number2
    def operation(self):
        if self.operator == "+":
            return self.sum()
        elif self.operator == "-":
            return self.subtraction()
        elif self.operator == "x" or self.operator =="*":
            return self.multiplication()
        elif self.operator == "/":
            return self.division()
        else:
            return "invalid operator"
        
number1 = float(input("enter a value: "))
operator = str(input("enter a operator (+)sum,(-)subtraction,(x)multiplication,(/)division: "))
number2 = float(input("enter the next value: "))

calc = calculator(number1, number2, operator)
result = calc.operation()
print(f"{number1} {operator} {number2} = {result}")