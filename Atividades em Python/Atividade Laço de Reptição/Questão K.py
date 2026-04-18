
def imprimir_divisores(numero):
    print(f"Os divisores de {numero} são:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i, end=", ")


numero = int(input("Digite um número positivo: "))


if numero > 0:
    imprimir_divisores(numero)
else:
    print("Por favor, digite um número positivo.")
