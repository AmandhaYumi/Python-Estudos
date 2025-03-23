#Tipos de dados
num_inteiro = 10
num_real = 3.14
texto = "Python"
logico = True e False
print(type(num_inteiro)) #Int
print(type(num_real)) #Float
print(type(texto)) #Str
print(type(logico)) #Bool

#Operadores Aritméticos
a = 10
b = 3
print(a + b) #Adição
print(a - b) #Subtração
print(a * b) #Multiplicação
print(a / b) #Divisão
print(a // b) #Divisão Inteira
print(a % b) #Resto da Divisão
print(a ** b) #Potência
"Atribuição adicionar = depois do sinal"

-------------------------------------------------------

#Comando print()
"O comando print() exibe informações na tela."
Ex:
print(‘Olá, mundo!’)

#Comando input()
"O comando input() recebe dados do usuário."
Ex:
nome = input('Digite seu nome: ')
print(f'Olá, {nome}!')

#Método format()
"Usamos .format() para substituir valores:"
Ex:
nome = 'Ana'
idade = 25
print('Meu nome é {} e tenho {} anos.'.format(nome, idade))

-------------------------------------------------------

#F-strings
"Usamos f antes da string:"
nome = 'Carlos'
idade = 30
print(f'Meu nome é {nome} e tenho {idade} anos.')

#Alinhamento de texto
"Alinhando textos"
Ex:
nome = 'Python'
print(f'{nome:<10}') # Alinhado à esquerda
print(f'{nome:^10}') # Centralizado
print(f'{nome:>10}') # Alinhado à direita

-------------------------------------------------------

#Formatação numérica
"Controlando casas decimais:"
Ex:
preco = 123.45678
print(f'Preço formatado: {preco:.2f}')

#1) Número inteiro com zeros à esquerda (4 casas)
num_int = 10
print(f'{num_int:04d}’) # 0010     
"Situações Prescisando de 0 a esquerda se usa d"

# 2) Número float com 3 casas decimais
temp = 3.141
print(f'{temp:.2f}') # 3.14
print(f'{temp:.4f}') # 3.1410
"Usa . + número de casas decimais solicitada + f"

# 3) Números formatados com tamanho 5
numeros = [10, 1, 333, 4500]
for num in numeros:
print(f'{num:5,.0f}'.replace(',', '.'))

# 4) Números float formatados com duas casas
num1 = 3.14
num2 = 5.678
num3 = 8.9
print(f'{num1:5.2f}'.replace('.', ',’)) # 3,14
print(f'{num2:5.2f}'.replace('.', ',’)) # 5,68
print(f'{num3:5.2f}'.replace('.', ',’)) # 8,90

#Alinhamento e formatação de números:
Ex:
num = 3000.98
print(f'{num:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.’))
3.000,98

------------------------------------------------------------------------------

#Estruturas condicionais
"As estruturas condicionais permitem que um programa tome decisões com base em condições."

#IF – ELIF - ELSE
• O IF verifica uma condição e executa um bloco de código
se for verdadeira.
• O ELIF permite testar múltiplas condições.
• O ELSE é executado se nenhuma das condições anteriores
for verdadeira.
Ex:
idade = int(input("Digite sua idade: "))
if idade < 18:
print("Você é menor de idade.")
elif idade < 60:
print("Você é adulto.")
else:
print("Você é idoso.")

#MATCH – CASE
• Ele permite comparar um valor com padrões específicos.
• O MATCH - CASE é mais eficiente e legível para
comparações diretas de valores.
• Use MATCH - CASE quando houver múltiplas opções fixas
Ex:
comando = input("Digite um comando: ")
match comando:
case "iniciar":
print("Iniciando...")
case "parar":
print("Parando...")
case "reiniciar":
print("Reiniciando...")
case _:
print("Comando desconhecido.")

#_ é usado como default em python pelo menos na situação case
