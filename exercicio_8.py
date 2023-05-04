#Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas#

x = float(input("Digite uma distância em Metros: "))
print(f"A distância de {x} corresponde a:")
print(f"{x / 1000} Km")
print(f"{x / 100} Hm")
print(f"{x / 10} Dam")
print(f"{x * 10} dm")
print(f"{x * 100} cm")
print(f"{x * 1000} mm")