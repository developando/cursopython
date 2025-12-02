"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
number = input('Digite um número: ')

try:
  if (int(number) % 2) == 0:
      print(f"Esse número é par {number}")
  else:
      print(f"Este número é impar {number}") 
except:
    print(f"numero digitado não é um valor inteiro ou não é um numero {number}")
"""
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input("Digite a hora: ")

if (int(hora)) <= 11:
    print(f"Bom dia, a hora atual é {hora}")
elif (int(hora)) <= 17:
    print(f"Boa tarde, a hora atual é {hora}")

else:
    print(f"Boa noite, a hora atual é {hora}")



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""
name = input ("Digite seu nome: ")

if len(name) <=4 :
    print (f"Seu nome é muito curto {name}")
elif len(name) <= 6 :
    print(f"Seu nome é normal {name}")
else:
    print(f"Seu nome é muito grande {name}")
"""