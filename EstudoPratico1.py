distancia = float(input("Digite uma distancia(d): "))
tempo = float(input("Digite uma tempo(s): "))
while tempo <= 0:
    print("Tempo inexistente, digite o tempo >0 ")
    tempo = float(input("Tempo(s)"))
v = distancia/tempo
print("Velocidade media(m/s) ", v)
 
if v >= 50:
    print("Voce esta acima da velocidade.")
else:
    print("Velocidade premitida.")

    #Danilo Landin de Vecchi Pestana
    #Data 04/03/2026
    #Turma ADS Noturno - Unidade Pinheiros