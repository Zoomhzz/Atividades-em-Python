def saudacao():
  pessoa = input("Bem-vindo(a) a calculadora inteligente🧮, Por favor informe seu nome:ㅤ")
  print(f"Olá {pessoa}, vamos começar?")
 
 
def somar(num1,num2):
  resultado = num1 + num2
  print(resultado)
  
def subtrair(num1,num2):
  resultado = num1 - num2
  print(resultado)
  
def multi(num1,num2):
  resultado = num1 * num2
  print(resultado)
  
def divi(num1,num2):
  resultado = num1 / num2
  print(resultado)


saudacao()
while True:   
  
 
 num_1 = float(input("Informe o 1° valor:\n"))
 num_2 = float(input("Informe o 2° valor:\n"))


 op = input ("Digite + para somar, Digite - para subtrair, Digite * para multiplicar, Digite / para dividir:ㅤ")

 match op:
   case "+":
    somar(num_1 , num_2) 
   case "-":
    subtrair(num_1 , num_2)
   case "*":
    multi(num_1, num_2)
   case "/":
    divi(num_1, num_2)
        
 final= input("Deseja continuar a usar a calculadora? (Sim ou Não):ㅤ")        
 if final.lower() !="sim":
  break