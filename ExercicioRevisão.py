#1. Converta corretamente e exiba o tipo resultante:
valor = "150.34"
novo_valor = float(valor)  # Completo com float()
print(type(novo_valor))


#2. Calcule o valor total de uma compra considerando
#um desconto de 10%.
valor = float(input("Digite um valor: "))
desconto = valor * 0.10  # Calculando 10% do valor
valor_com_desconto = valor - desconto  # Subtraindo o desconto do valor original
print(f'Valor com desconto: {valor_com_desconto}')


#3. Crie um programa que calcule a média de 3 notas e
#verifique se a média é maior que 7
NotaX = float(input("Digite a 1 prova: "))
NotaY = float(input("Digite a 2 prova: "))
NotaZ = float(input("Digite a 3 prova: "))
Média = (NotaX + NotaY + NotaZ) / 3
if (Média > 7):
    print("Média maior que sete!")
else:
    print("Média não e maior que sete!")


#1. Peça um nome e uma idade e exiba a mensagem formatada.
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
print('Meu nome é {} e tenho {} anos.'.format(nome, idade))


#2. Peça um número decimal e mostre-o com 2 casas decimais.
Numero = float(input("Digite um número decimal: "))
print(f'Número formatado: {Numero:.2f}')


#3. Formate um texto centralizado em 20 caracteres.
texto = 'Frase De 20 caracteres.'
print(f'{texto:^30}')  