salario = float(input("Digite seu salario: "))
if salario < 2000.00:
    print("Nao pagara imposto!")
else:
    print("Devera pagar imposto")


a = (5)
b = (1)
c = True
d = True

if a>b and c or d:
    print("Resultado é verdadeiro.")
else:
    print("Resultado é falso.")
    #Resultado falso
#Resultado falso
    #Verdadeiro


materia1 = float(input("Digite sua nota na materia 1: "))
materia2 = float(input("Digite sua nota na materia 2: "))
materia3 = float(input("Digite sua nota na materia 3: "))
media = ((materia1 + materia2 + materia3)/3)
print(f"Sua media é: {media}.2f")

if media >= 7:
    print("Voce esta aprovado")
else:
    print("Voce esta reprovado")