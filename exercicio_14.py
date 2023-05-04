#A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva 
#um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, 
#sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

kmPercorridos = float(input("Quantos KM foram percorridos?: "))
diasAlugados = int(input("Foi alugado por quantos dias?: "))

total_diasAlugado = diasAlugados * 90
total_kmPercorridos = kmPercorridos * 0.20

print(f"Total a pagar por dia alugado: R${total_diasAlugado}")
print(f"Total a pagar por Km rodado: R${total_kmPercorridos}")
print(f"Total a pagar: R${total_diasAlugado + total_kmPercorridos}")