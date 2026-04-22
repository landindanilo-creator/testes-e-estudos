cadastro_clientes = []
cadastro_cpf = []
cadastro_telefone = []
cadastro_celular = []
cadastro_endereco = []
cadastro_cep = []

#Função para cadastro
def cadastro_cliente(nome, cpf, telefone, celular, endereco):
    cadastro_clientes.append(nome)
    cadastro_cpf.append(cpf)
    cadastro_telefone.append(telefone)
    cadastro_celular.append(celular)
    cadastro_endereco.append(endereco)
    
    nome = input("Digite seu nome completo: ")
    cpf = int(input("Digite seu CPF: "))
    telefone = int(input("Digite seu telefone: "))
    celular = int(input("Digite seu celular: "))
    endereco = input("Digite seu endereço: ")

#Lista de clientes
def lista_clientes():
    print("Lista de clientes cadastrados:")
    for i in range(len(cadastro_clientes)):
        print(f"Nome: {cadastro_clientes[i]}\n, CPF: {cadastro_cpf[i]}\n, Telefone: {cadastro_telefone[i]}\n, Celular: {cadastro_celular[i]}\n, Endereço: {cadastro_endereco[i]}")

#Menu de opções
print("Bem Vindo ao sistema de cadastro de clientes!")
print("1 - Cadastrar Cliente")
print("2 - Lista de Clientes")
print("3 - Sair")
opc = int(input("Escolha uma opção: "))

while opc != 3:
   
    
    #Menu de opções
    if opc == 1:
        cadastro_cliente("", 0, 0, 0, "")

    elif opc == 2:
        lista_clientes()

    elif opc == 3:
        print("Encerrando o programa!")
        break
    else:
        print("Opção invalida! Escolha outra opção.")

    

