cadastro_nome = []
cadastro_cpf = []
cadastro_telefone = []
cadastro_celular = {}
cadastro_endereco = []
cadastro_cep = []

def cadastro_cliente(cadastro_nome, cadastro_cpf, cadastro_telefone, cadastro_celular, cadastro_endereco):
    cadastro_nome ==input("Digite seu nome completo: ")
    cadastro_cpf == int(input("Digite seu CPF: "))
    cadastro_telefone = int(input("Digite seu telefone"))
    cadastro_celular = int(input("Digite seu celular: "))
    endereco = input("Digite seu endereço: ")

while True:
    print("Bem Vindo ao sistema de cadastro de clientes!")
    print("1 - Cadastrar Cliente")
    print("2 - Lista de Clientes")
    print("3 - Sair")
    opc = int(input("Escolha uma opção!"))
    
    if opc == 1:
        cadastro_cliente(cadastro_nome, cadastro_cpf, cadastro_telefone, cadastro_celular, cadastro_endereco)
        print("Cadastro bem sucedido!")
    elif opc == 2:
        cadastro_cliente(cadastro_nome, cadastro_cpf, cadastro_telefone, cadastro_celular, cadastro_endereco)
        print("Lista de Cadastro de clientes!")
        for i in range(len(cadastro_nome[i])):
            print(f"Nome: {cadastro_nome[i]}")
        for i in range(len(cadastro_cpf[i])):
            print(f"CPF: {cadastro_cpf[i]}")
        for i in range(len(cadastro_telefone[i])):
            print(f"Telefone: {cadastro_telefone[i]}")
        for i in range(len(cadastro_celular[i])):
            print(f"Celular: {cadastro_celular[i]}")
        for i in range(len(cadastro_endereco[i])):
            print(f"Endereço: {cadastro_endereco[i]}")

    elif opc == 3:
        print("Encerrando sistema!")
        break