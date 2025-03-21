#1) Peça ao usuário para digitar uma nota de 0 a 10 e classifique-a da seguinte forma:
#- Nota ≥ 9 → "Excelente"
#- Nota ≥ 7 → "Bom"
#- Nota ≥ 5 → "Regular"
#- Nota < 5 → "Reprovado"
Nota = int(input("Digite sua nota: "))
if(Nota >= 9):
    print("Excelente")

elif(Nota >=7):
    print("Bom")

elif (Nota >=5):
    print("Regular")

else:
    print("Reprovado")
#else + if -> elif (python)
#else if -> (java)


#2) Solicite um número inteiro ao usuário e diga se ele é par ou ímpar.
#Dica: Use o operador % (módulo) para verificar se o número é divisível por 2.
Numero = int(input("Digite um numero: "))
if(Numero % 2 == 0):
    print("Par")
else:
    print("Impar")
# numero = 2 -> númeor É igual a 2
# numero == 2 -> Número é igual a 2? 


#3) Cálculo de IMC - Peça ao usuário para informar peso (kg) e altura (m), calcule o IMC
#e classifique:
#- IMC < 18.5 → "Abaixo do peso"
#- IMC entre 18.5 e 24.9 → "Peso normal"
#- IMC entre 25 e 29.9 → "Sobrepeso"
#- IMC ≥ 30 → "Obesidade"
#Fórmula do IMC: IMC = peso / (altura ** 2)
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso / (altura ** 2)
if(IMC < 18.5):
    print("Abaixo do peso")
elif(IMC > 18.5 and IMC < 24.9):
    print("Peso normal")
elif(IMC > 25 and IMC < 29.9):
    print("Sobrepeso")
else:
    print("Obesidade")


#4) Peça três números ao usuário e mostre qual deles é o maior.
#Dica: Use `if - elif - else` para comparar os valores.
NumeroX = float(input("Digite o 1 número: "))
NumeroY = float(input("Digite o 2 número: "))
NumeroZ = float(input("Digite o 3 número: "))
if(NumeroX > NumeroY and NumeroX > NumeroZ):
    print(f"O número {NumeroX} é o maior")
if(NumeroY > NumeroX and NumeroY > NumeroZ):
    print(f"O número {NumeroY} é o maior")
if(NumeroZ > NumeroX and NumeroZ > NumeroY):
    print(f"O número {NumeroZ} é o maior")


#5) Solicite as notas de três provas e calcule a média do aluno.
#Se a média for maior ou igual a 6, o aluno está aprovado, caso contrário, reprovado.
#Dica: (nota1 + nota2 + nota3) / 3
NotaX = float(input("Digite a 1 prova: "))
NotaY = float(input("Digite a 2 prova: "))
NotaZ = float(input("Digite a 3 prova: "))
Média = (NotaX + NotaY + NotaZ) / 3
if(Média >= 6):
    print("Aprovado")
else:
    print("Reprovado")

