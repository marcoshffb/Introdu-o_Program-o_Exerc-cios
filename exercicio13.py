salario = float(input("Digite seu salário mensal: "))
if salario <= 2000:
    print("Você está isento de imposto!")
elif salario >= 2000.01 and salario <= 3500:
    print(salario * 0.1)
else: print(salario * 0.15)