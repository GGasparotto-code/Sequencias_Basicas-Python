#Crie um programa que leia o preço de um produto, calcule e mostre o seu 
#PREÇO PROMOCIONAL, com 5% de desconto.

preco = float(input("Digite o valor do produto [R$]: "))
desconto = float(input("Digite o percentual de desconto [%]: "))

valorDesconto = preco * desconto/100
valorPagar = preco - valorDesconto

print(f"Valor mercadoria: R${preco:.2f}")
print(f"Desconto: {desconto:.2f}% - R${valorDesconto:.2f}")
print(f"Total a pagar : R${valorPagar:.2f}")