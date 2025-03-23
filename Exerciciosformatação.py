#1) Peça ao usuário um número decimal e exiba-o formatado com duas casas decimais.
#Exemplo:
#Entrada: 12.3456 → Saída: 12.35
#Dica: Use f-string ou format().
valor = float(input("Digite um valor: "))
print(f"valor: {valor:.2f}")


#2) Peça ao usuário um valor e exiba-o formatado como moeda brasileira (R$).
#Exemplo: Entrada: 1500.5 → Saída: R$ 1.500,50
dinheiro = float(input("Digite um valor: "))
print(f"Dinheiro formatado: {dinheiro:,.2f}".replace(",","x").replace(".",",").replace("x","."))


#3) Solicite um número inteiro ao usuário e exiba-o sempre com 5 dígitos, preenchendo 
#com zeros à esquerda.
#Exemplo: Entrada: 42 → Saída: 00042
ex3 = int(input("Digite um valor: ")) ##10 -> 00010
print(f"a direita: {ex3:05d}") 


#4) Peça um número ao usuário e exiba-o formatado em notação cienSfica.
#Exemplo: Entrada: 123456789 → Saída: 1.23e+08
#Dica: Use e na formatação.
ex4 = int(input("Digite um valor (4): "))
print(f"notação cientifica: {ex4:e}")


#5) Exibir um número com separadores de milhar
#Solicite um número inteiro e exiba-o formatado com separadores de milhar (1.000.000).
#Exemplo: Entrada: 1000000 → Saída: 1,000,000
ex5 = int(input("Digite um valor (5): "))
print(f"milhar: {ex5:,}")


#6) Converter uma string para maiúsculas, minúsculas e capitalizada
#Peça ao usuário para digitar um texto e exiba:
#• Tudo em maiúsculas
#• Tudo em minúsculas
#• Somente a primeira letra em maiúscula
#Exemplo: Entrada: "python é incrível"
#Saída: MAIÚSCULAS: PYTHON É INCRÍVEL 
#minúsculas: python é incrível 
#Capitalizado: Python é incrível 
#Dica: Use upper(), lower() e capitalize()
frase = input("Escreva uma frase: ")
print(f"LETRA MAIUSCULA: {frase.upper()}")
print(f"letra minusculo: {frase.lower()}")
print(f"Somente primeira letra em maiusculo: {frase.capitalize()}")




