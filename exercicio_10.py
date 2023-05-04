#Faça um algoritmo que leia a largura e altura de uma parede, calcule e 
#mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, 
#sabendo que cada litro de tinta pinta uma área de 2metros quadrados

x = float(input("Largura da parede: "))
y = float(input("Altura da parede: "))
print(f"A área a ser pintada é de {y * x} Metros")
print(f"A quantidade de tinta necessária são {(x * y) / 2} litros")