#Exercícios com MATCH - CASE 
#6) Peça ao usuário para digitar uma cor do semáforo ("vermelho", "amarelo" ou 
#"verde") e exiba a ação correspondente: - "Vermelho" → "Pare!" - "Amarelo" → "Atenção!" - "Verde" → "Siga!" - Qualquer outra entrada → "Cor inválida!" 
#Dica: Use match - case para comparar as cores. 
comando = input("Digite uma cor do semáforo: ")

match comando:
    case "Vermelho":
        print("Pare!")
    case "Amarelo":
        print("Atenção!")
    case "Verde":
        print("Siga!")
    case _:
        print("Cor inválida!")


#7) Peça ao usuário para digitar uma operação matemática básica ("+", "-", "*", "/"). 
#Solicite dois números e realize a operação escolhida. 
#Caso o usuário digite um operador inválido, exiba "Operação não reconhecida". 
# Solicita a operação matemática
operacao = input("Digite uma operação matemática (+, -, *, /): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

match operacao:
    case "+":
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    case "/":
        if num2 != 0:  
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro não da pra dividir por zero!")
    case _:
        print("Operação não reconhecida")

        
#8) Solicite um nome de animal ao usuário e diga a que grupo ele pertence: 
#- "cachorro", "gato", "leão" → "Mamífero" 
#"cobra", "lagarto" → "Réptil"
#- "águia", "papagaio" → "Ave"
#- Qualquer outra entrada → "Desconhecido" 
comando = input("Escolha um animal: ")

match comando:
    case "cachorro" | "gato" | "leão" :
        print("Mamifero!")
    case "cobra" | "lagarto":
        print("Réptil!")
    case "águia" | "papagaio":
        print("Ave!")
    case _:
        print("Desconecido!")


#9) Peça ao usuário para escolher um personagem digitando um número de 1 a 3: 
#1 → "Você escolheu o Guerreiro!" 
#2 → "Você escolheu o Mago!" 
#3 → "Você escolheu o Arqueiro!" 
#Qualquer outro número → "Opção inválida!"
comando = input("Escolha um numero de 1 a 3: ")

match comando:
    case "1":
        print("Você escolheu o Guerreiro!")
    case "2":
        print("Você escolheu o Mago!")
    case "3":
        print("Você escolheu o Arqueiro!")
    case _:
        print("Opão inválida")
        

#10) Peça ao usuário para digitar uma nota de 0 a 10 e converta essa nota em um 
#conceito, seguindo a seguinte tabela. 

#Nota           Conceito
#9 ou 10            A
#7 ou 8             B
#5 ou 6             c
#3 ou 4             D
#0 ou  ou 2         E
nota = int(input("(5) Digite a nota: "))

match(nota):
    case 9 | 10:
        print("A")
    case 7 | 8:
        print("B")
    case 5 | 6:
        print("C")
    case 3 | 4:
        print("D")
    case 0 | 1 | 2:
        print("E")

