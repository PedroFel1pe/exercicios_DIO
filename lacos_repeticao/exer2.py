# 2. Menu com opções:  Adicionar item (exibe "Item adicionado"), Ver mensagem (exibe "Olá!"), Sair do programa
item = []
while True:
    print("Selecione uma das opções:")
    print("1-Adicionar item")
    print("2-Ver lista de itens")
    print("3-Sair")
    opcao = int(input("Qual opção escolhida:"))

    if opcao == 1:
        item2 = input("Escreva qual item a ser adicionado:").strip().lower()
        item.append(item2)
        print("Item adicionado")
    elif opcao == 2:
        print("Olá, aqui esta sua lista de itens:")
        print(",".join(item))
    elif opcao == 3:
        print("Saindo....")
        break
    else:
        print("Opção invalida, digite de 1 a 3 conforme o que for de seu interese.")