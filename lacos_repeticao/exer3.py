# 3. Login com tentativas: Simule um sistema de login com senha fixa (1234). O usuário tem 3 tentativas. Se errar, exibe "Acesso bloqueado". Se acertar, "Bem-vindo!"
# depois que fiz ó codigo que entendi o conceito de senha fixa e sua importancia, porém como ja fiz esse pequeno codigo de cadastro vou manter assim mesmo. 
print("criando login")
nome = input("Nome de usuario: ").strip().lower()
senha = input("Senha: ")
print("/--/" * 5)
tentativa = 1 # maximo de 3 tentativas, deixei 1 porque se a pessoa errar a primeira ja sera contado
while True:
    print("Fazer login")
    nome2 = input("Nome de usuario: ").strip().lower()
    senha2 = input("Senha: ")
    if nome == nome2 and senha == senha2:
        print("Bem Vindo!!!")
        break
    elif tentativa < 3:
        print(f"Nome ou Senha incorreto, {3 - tentativa} tentativa(s) restante(s)")
        tentativa += 1
    else:
        print("Conta Bloqueada")
        break
