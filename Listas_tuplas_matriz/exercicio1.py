#Crie uma lista com 5 números inteiros e:

numeros = [9,4,6,5,6,1]

# Imprima todos os elementos

print(f"lista original: {numeros}")

# Some todos os valores

soma = sum(numeros)
print(f"soma dos numeros da lista: {soma}")

# Mostre o maior e o menor número

numeros_organizados = sorted(numeros)
print(f"lista de numeros organizados: {numeros_organizados}")
print(f"menor numero:{numeros_organizados[0]}") # print(f"Menor número: {min(numeros)}")
print(f"maior numero:{numeros_organizados[-1]}") # print(f"Maior número: {max(numeros)}")