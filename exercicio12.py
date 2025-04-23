l1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
l2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
l3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))
if l1 == l2 and l3:
    print("O triângulo é equilátero!")
elif l1 != l2 != l3:
    print("O triângulo é escaleno!")
else:
    print("O triêngulo é isósceles!")