
def soma_divisores(numero):
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma += i
    return soma


numero = int(input("Digite um número inteiro: "))


resultado = soma_divisores(numero)


print(f"A soma dos divisores de {numero}, excluindo o próprio número, é: {resultado}")
