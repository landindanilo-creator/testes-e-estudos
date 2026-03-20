#Programa que diz se o carro é novo ou velho
ano_carro = int(input("Digite o ano de seu carro: "))
ano_compra = int(input("Qual o ano de compra: "))
idade_carro = (ano_compra - ano_carro)
print(f"a idade de seu carro é: {idade_carro} anos")
if idade_carro <= 2:
    print("Seu carro é novo!")
elif idade_carro <= 4 and idade_carro >=3:
    print(f"Seu carro é seminovo! {idade_carro}")
elif idade_carro >= 5:
    print("Seu carro é velho!")
else:
    print("Valor invalido")