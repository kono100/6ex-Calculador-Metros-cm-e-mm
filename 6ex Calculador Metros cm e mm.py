

#6. Faça um programa que leia uma quantidade X de metros e retorne o equivalente em:
# cm
# mm


Metros = float(input("Digite Quantos Metros: "))
#Salario1=(Salario*25/100)
#TOTAL = (Salario+Salario1)
cm = Metros*100
mm = Metros*1000
print(f"\nEm Metros {Metros}\n")
print(f"Em cm {cm:,.0f}\n")
print(f"Em mm {mm:,.0f}\n")