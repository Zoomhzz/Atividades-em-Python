ifestas= []
for i in range (5):
    valor = input(f"Digite o {i+1}º item:")
    ifestas.append(valor)



pesquisar = (input("Informe o item a ser encontrado"))
if pesquisar in ifestas :
    print ("O", pesquisar, "foi encontrado na lista")
else:
    print ("O",pesquisar, "Não foi encontrado")

    
ei= int(input("Informe os itens escolhidos, digite 1 para finalizar seu pedido ou 2 para continuar com seu pedido"))
item2= input("Escreva o item a se adicionar")
item2_lista = []
match ei:
    case 1:
        print("Pedido Finalizado")
    case 2:
        ifestas.append(item2)  
        print("Pedido Finalizado", "O item", item2, "Foi adicionado a lista")
tuple_ifestas = tuple(ifestas)  
print(tuple_ifestas)  

print("Obrigado por pelo pedido 😉")