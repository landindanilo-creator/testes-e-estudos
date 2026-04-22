'Tranforme polegada em centimetro, ou vice e versa'

centimetro = float(input("Digite um valor em medida: "))
polegada = 2.4
resultado_polegada = (centimetro / polegada)
resultado_centimetro = centimetro * polegada 

if resultado_polegada >= 2.4:
    print("Valor da medida em polegada: ")
elif resultado_centimetro >= 0:
    print("Valor da medida em centimetros: ")
else:
    print("Valor invalido")
    
#Diga uma medida:
#Se medida for:
#centimetro/polega
#Resultado =  polegada
#Senão 
#centimetro*polegada

