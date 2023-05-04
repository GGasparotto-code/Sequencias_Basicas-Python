#Escreva um programa para calcular a redução do tempo de vida de um 
#fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele 
#já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule 
#quantos dias de vida um fumante perderá e exiba o total em dias.

cigarroDia = int(input("Quantidade de cigarros fumados por dia: "))
tempoFumando = float(input("Quantidade de anos que é fumante: "))
tempoPerdido = (cigarroDia * 365 * tempoFumando * 10) / (24 * 60)

print(f"Pessoa fumou: {tempoFumando} anos, {cigarroDia} cigarros/dia")
print(f"Perdeu em média: {tempoPerdido:.1f} dias de vida")