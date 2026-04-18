
soma = 0

contador = 0


for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro positivo: "))
    
    if numero > 0:
        soma += numero
        contador += 1
    else:
        print("Número não positivo, será ignorado.")


if contador > 0:
    
    media = soma / contador
    print(f"A média dos números positivos é: {media}")
else:
    print("Nenhum número positivo foi inserido.")
