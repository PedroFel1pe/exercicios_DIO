#Crie uma matriz 3x3 (lista de listas), peça ao usuário para digitar os valores de cada posição e:
#Use dois for aninhados para preencher e outro para exibir.
matriz = []
for i in range(3):
    numero = input("informe 3 numeros separados por virgula: ")
    lista_numero = numero.split(",")
    lista_numero = [int(num) for num in lista_numero]  # converte para int
    matriz.append(lista_numero)

#Mostre a matriz no formato 3x3.

for linha in matriz:
    for valor in linha:
        print(valor, end = " ")
    print()

#Some todos os valores.

soma1 = sum(matriz[0])
soma2 = sum(matriz[1])
soma3 = sum(matriz[2])
print(f"soma: {soma1 + soma2 + soma3}")

#Mostre os valores da diagonal principal.

print(matriz[0:0])
print(matriz[1:1])
print(matriz[2:2])
    