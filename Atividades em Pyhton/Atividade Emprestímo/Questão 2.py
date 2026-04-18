n1 = int(input("Informe a nota 1: "))
n2 = int(input("Informe a nota 2: "))
n3 = int(input("Informe a nota 3: "))
n4 = int(input("Informe a nota 4: "))


media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print("Aluno aprovado")
elif media >= 5:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")
    
    ntr = float(input("Informe sua nota da recuperação"))
    
    ntr= media + ntr/4
    
    if ntr >= 5:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")
        
