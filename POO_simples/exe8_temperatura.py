#converter Celsius para Fahrenheit, e agora adicione o método para converter Fahrenheit para Celsius.
class Temperature:
    def convert_celsius(self,celsius):
        result = (celsius * 1.8) + 32
        return f"{celsius}°C = {result:.2f}°F"
    def convert_fahrenheit(self,fahrenheit):
        result = (fahrenheit - 32) / 1.8
        return f"{fahrenheit}°F = {result:.2f}°C"

temperature = Temperature()
option = input("Type 1 to change from Celsius to Fahrenheit or type 2 to change from Fahrenheit to Celsius: ")
if option == "1":
    celsius = float(input("Enter the temperature in Celsius: "))
    print(temperature.convert_celsius(celsius))
elif option == "2":
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    print(temperature.convert_fahrenheit(fahrenheit))
else:
    print("Value invalid")
