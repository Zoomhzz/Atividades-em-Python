def ola ():
    nome = input("Por favor,Informe seu nome:ﾠ")
    print(f"Seja Bem vindo ao sistema de médias {nome}")
    
def calculo_media(n1,n2,n3):
    
    media = (n1 + n2 + n3) / 3
    if media < 7 and media >= 5:
        print(f"Sua média é, {media:.2f}, Aluno em recuperação")
    elif media < 5:
        print(f"Sua média é, {media:.2f}, Aluno reprovado")
    else:
        print(f"Sua média é, {media:.2f} , Aluno aprovado, parabéns 😉👩‍🏫")

    
    
def consulta_media (n1,n2,n3):
    
    media= (n1+n2+n3)/3
    print(f"Aqui está sua média, é {media:.2f}")
    
ola()
while True:
 
 op = input("II====Para consultar sua média Digite 1====II\nII====Para calcular sua média Digite 2====II\n: ")

 nota1 = float(input("Informe sua 1° nota 🗒️: "))
 nota2 = float(input("Informe sua 2° nota 🗒️: "))
 nota3 = float(input("Informe sua 3° nota 🗒️: "))

 match op:
    case '1':
        consulta_media(nota1, nota2, nota3)
    case '2':
        calculo_media(nota1, nota2, nota3)
    case _:
        print("Opção inválida.")

 final= input("Deseja continuar a usar a calculadora? (Sim ou Não):ㅤ")        
 if final.lower() !="sim":
  break