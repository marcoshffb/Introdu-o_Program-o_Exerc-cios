s = input("Digite uma frase: ")

def conta_vogais(s):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in s:
        if char in vogais:
            contador += 1
    return contador

print(conta_vogais(f"{s}"))
