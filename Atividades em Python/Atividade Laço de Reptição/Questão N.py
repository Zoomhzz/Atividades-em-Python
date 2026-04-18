numero= int(input("Informe a quantidade de termo da sequência de Fibonacci"))
termo_inicio = 0
termo_fim = 1
i= 0

while i <= numero:
    termo = termo_inicio + termo_fim
    print(termo)
    termo_inicio = termo_fim
    termo_fim = termo
    i = i + 1