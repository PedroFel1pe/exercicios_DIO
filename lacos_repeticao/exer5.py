# 2. Tabuada personalizada: Peça ao usuário um número e mostre a tabuada de 1 a 10 com for
numero = int(input("Informe um numero inteiro:"))
for tabuada in range(1,11):
    print(f"{numero} x {tabuada} = {numero * tabuada}")