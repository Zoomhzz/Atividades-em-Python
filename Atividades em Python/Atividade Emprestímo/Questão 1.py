Em=float (input("Informe o valor desejado do émprestimo"))
sl_mensal= float(input("Informe sua renda mensal"))
qtd_p= int (input("informe a quantidade de parcelas de 6 a 48 "))

juros= Em / qtd_p
x= sl_mensal * 0.40 

if (juros <= x):
    print ("Os juros do seu émprestimo serão R$:")
    print ("Émprestimo aceito")
else:
    print("Émprestimo negado")
    
if(qtd_p >=6) or (qtd_p <= 12):
    print ("Os juros a serem pagos serão de R$: " , Em * 0.015)
elif(qtd_p >=12) or (qtd_p <=24 ):
    print("Os juros a serem pagos serão de R$:" , Em * 0.20)
else :(qtd_p >= 24) or (qtd_p <= 48)
print ("Os juros a serem pagos serão de R$:" , Em *  0.25)

if print:
    ("Émprestimo negado")
    