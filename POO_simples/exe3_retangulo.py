#Crie uma classe Retangulo que tenha atributos largura e altura. Crie métodos para:Calcular a área.Calcular o perímetro.Verificar se o retângulo é um quadrado
#vou programar em inglês para praticar

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return 2*(self.width + self.height)
    def square(self):
        if self.width == self.height:
            return "square"
        return "rectangle"
width = float(input("Enter a widht: "))
height = float(input("Enter a height:"))
rectangle = Rectangle(width, height)
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()
shape_type = rectangle.square()
print(f"This shape has a width of {width} cm and a height of {height} cm making it a {shape_type}.")
print(f"It has an area of {area} m² and a perimeter of {perimeter} cm.")
