n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

resultado = n1 + n2
print(resultado)

#tranformação de metros em milimetros
metro = float(input("Digite um valor em metro(m) para transformar em milimetros: "))
milimetro = 0.001
transformacao =  metro / milimetro
print(f"Resultado da transformação para milimetros(mm) é: {transformacao: .2f}")

#programa para mostrar dias, horas, segundos e mostrar os segundos totais 
dias = int(input("Digite dias: "))
horas = int(input("Digite horas: "))
minutos = int(input("Digite minutos"))
segundos = int(input("Digite segundos: "))

#Conversão para segundos
total_segundo = (dias * 24 * 3600) + (horas * 3600) + (minutos * 60) + (segundos)

#Total em segundosu
print(f"Total em segundos é: {total_segundo: .2f}")



#Programa para calcular aumento de salario 
salario = float(input("Digite o valor de seu Salario: R$"))
aumento = 15

salario_atual = salario * (1 + aumento / 100)
print("Salario atual é: R$", salario_atual)


#programa para desconto

mercadoria = str(input("Escolha uma mercadoria: "))
custo_mercadoria = 750.00
desconto = 12
print("mercadoria escolhida é",mercadoria, "Custo: ",custo_mercadoria)
desconto = custo_mercadoria * (1 - desconto / 100 )

print(f"Valor de mercadoria com descoto é: ",mercadoria, desconto )


#programa medidor de distancia e velocidade

velocidade = float(input("Diga a velocidade esperada para a chegada ao ponto"))
distancia = float(input("Qual a distancia deseja percorrer(km): "))

tempo_percorrido = distancia / velocidade
print("O tempo estimado para essa viagem é de: hrs", tempo_percorrido)

#Transformacao em termometro
temperatura = float(input("Digite sua temperatura em C°: "))
temp_f = ((9 * temperatura)/5)+32
print("Sua temperatura em F° é : ", temp_f)



#Programa carro alugado
carro = int(input("Quanto tempo vc aluga esse carro(dias): "))
km = float(input("Quantos km vc ja percorreu com esse carro? "))
valor_carro = (carro * 60)
print("Valor gasto ao total de dias alugado é: ", valor_carro)
valor_km = (km * 0.15)
print("Valor total gasto em gasolina por km é: ", valor_km)
gasto_total =  valor_km + valor_carro
print("Gasto total com o alugel é de : ", gasto_total)


#programa de expectativa de vida 
quanti_cigarro = int(input(("Quantos cigarros voce fuma por dia? ")))
anos_fumando = int(input("A quantos anos voce fuma? "))
resultado_fumar = (quanti_cigarro * anos_fumando * 365)/1440
print(f"Resultado de anos fumando, dias perdidos é aproximadamente: {resultado_fumar: .0f}")
