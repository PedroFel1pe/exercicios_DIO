#Crie uma classe Veiculo com atributos como marca, modelo, ano e métodos para acelerar, frear e mostrar informações do veículo
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def accelerate(self):
        print(f"The {self.model} is accelerating...")
    def brake(self):
        print(f"The {self.model} is braking...")
    def vehicle_information(self):
        return f" Brand: {self.brand}\n Model: {self.model}\n Year: {self.year}"
    
vehicle = Vehicle("Chevrolet", "Vectra", 2000)
vehicle.accelerate()
vehicle.brake()
print(vehicle.vehicle_information())