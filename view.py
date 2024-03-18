from controller import *
while True:
    print("============ menu ============")
    decisao = int(input("1 - Cadastrar\n2 - Login\n3 - Sair\n"))
    
    if decisao == 1:
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        print(ControllerCadastro.cadastrar(nome, email, senha))
        break
    elif decisao == 2:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        print(ControllerLogin.login(email, senha))
        break
        
    elif decisao == 3:
        break