# 1. Soma até zero: Peça números ao usuário e some até que ele digite 0. Depois, mostre o total somado
result = 0
while True:
    number = int(input("Enter a number: "))
    
    if number == 0:
        print(f"The sum of all number is {result}")
        break
    result += number
