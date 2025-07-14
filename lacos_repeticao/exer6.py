# 3. Fatorial de um número: Peça um número e calcule o fatorial usando for
numero = int(input("Informe um numero inteiro: "))
resultado = 1
for fatorial in range(numero, 0, -1):
    resultado *= fatorial
    print(fatorial)
print(resultado)