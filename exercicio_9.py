#Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45#

reais = float(input("Quanto você tem na carteira?: "))
dolares = reais / 5.02
dolares_redondos = "{:.2f}".format(dolares)
print(f"Você pode comprar US$ {dolares_redondos}")