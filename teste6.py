def vericar_velocidade(velocidade, limite):
    if velocidade <= limite:
        print("Velocidade dentro do limite permitido!")
    else: 
        exesso = velocidade - limite  
        multa = exesso * 8 #multa por km acima da velocidade

        print(f"Velocidade acima do limite permitido! Multa de R$ {multa: .2f}")
        print(f"Excesso de velocidade: {exesso: .2f} km/h")

limite_permitido = 60 #km/h limite permitido
velocidade  = float(input("Digite a velocidade aproximada do carro: "))
vericar_velocidade (velocidade, limite_permitido)
viagem = float(input("Quantos quilometros tem a viagem: "))
tempo = viagem / velocidade

print(f"Tempo aproximado da viage é: {tempo: .2f}horas")
print("Boa viagem!")