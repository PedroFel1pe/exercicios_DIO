#Peça ao usuário para digitar números separados por vírgula:

numeros = input("informe numeros separando por ',': ")

#Salve os números numa lista

lista_numeros = numeros.split(",") #remove as ','

#Converta essa lista para uma tupla

tupla_numeros = tuple(lista_numeros)

#Mostre o tipo de cada estrutura
 
print(f"lista: {lista_numeros} (tipo: {type(lista_numeros)})")
print(f"tupla: {tupla_numeros} (tipo: {type(tupla_numeros)})")