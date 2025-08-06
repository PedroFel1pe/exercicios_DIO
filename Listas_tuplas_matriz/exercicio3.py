#Crie uma tupla com os dias da semana. Depois:

semana = ("domingo","segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira","sabado")

#Peça ao usuário um número de 1 a 7 e mostre o dia correspondente

opcao = int(input("informe um numero de 1 a 7, para saber a qual dia da semana corresponde:"))

if opcao == 1:        
    print(semana[0])            
elif opcao == 2:            
    print(semana[1])            
elif opcao == 3:
    print(semana[2])
elif opcao == 4:
    print(semana[3])
elif opcao == 5:
    print(semana[4])
elif opcao == 6:
    print(semana[5])
elif opcao == 7:
    print(semana[6])
else:
    print("numero incompativel")

#forma mais simples:

#if 1 <= opcao <= 7:
#    print(f"O dia correspondente é: {semana[opcao - 1]}")
#else:
#    print("Número incompatível.")