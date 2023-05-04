#Crie um programa que leia o número de dias trabalhados em um mês e mostre o 
#salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 
#por hora trabalhada.

diasTrabalhados = int(input("Quantidade de dias trabalhados em um mês: "))
salarioDiario = 25 * 8

print(f"Salário: R${salarioDiario * diasTrabalhados}")