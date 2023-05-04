#Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o 
#seu novo salário, com 15% de aumento.

salario = float(input("Entre com o salário atual R$: "))
aumento = float(input("Entre com o aumento %: "))

parcelaAumento = salario * aumento/100
novoSalario = salario * parcelaAumento

print(f"R${salario:.2f} com aumento de {aumento:.2f}% = R${novoSalario:.2f}")
print(f"Diferença de R${parcelaAumento:.2f}")