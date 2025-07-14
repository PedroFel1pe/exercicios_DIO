#Crie uma classe Contato com nome, telefone e e-mail. Depois crie uma classe Agenda que armazena vários contatos e tem métodos para adicionar, remover e buscar contatos.
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def contato_completo(self):
        return f"Nome:{self.nome}, Tel:{self.telefone}, e-mail:{self.email}"
    
class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def remover_contato(self, nome):
        self.contatos = [c for c in self.contatos if c.nome != nome]

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None
    
agenda = Agenda()
while True:
    print("\nMENU")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Listar todos os contatos")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        nome = input("Nome: ").strip().upper()
        telefone = input("Telefone: ").strip()
        email = input("E-mail: ").strip()
        contato = Contato(nome, telefone, email)
        agenda.adicionar_contato(contato)
        print("Contato adicionado com sucesso.")
        
    elif opcao == "2":
        nome = input("Nome do contato para remover: ").strip().upper()
        agenda.remover_contato(nome)
        print("Contato removido (se existia).")

    elif opcao == "3":
        nome = input("Nome do contato para buscar: ").strip().upper()
        resultado = agenda.buscar_contato(nome)
        if resultado:
            print("Contato encontrado:")
            print(resultado.contato_completo())
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        print("\nContatos na agenda:")
        if not agenda.contatos:
            print("Nenhum contato cadastrado.")
        for contato in agenda.contatos:
            print(contato.contato_completo())

    elif opcao == "5":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")