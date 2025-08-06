#Peça ao usuário para digitar 3 nomes e salve numa lista. Depois:

lista_nomes = []
while True:
    nome = str(input("digite o nome ou sair para encerrar: ")).lower()
    if nome == "sair":
        break
    else:
        lista_nomes.append(nome)
    
    

#Mostre os nomes em ordem alfabética

lista_nomes.sort()
print(f"Lista de nomes em ordem alfabetica: {lista_nomes}")

#Mostre quantos nomes tem a lista

tamanho_lista = len(lista_nomes)
print(f"A lista tem o total de: {tamanho_lista} nomes")
