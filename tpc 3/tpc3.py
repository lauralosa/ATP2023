#TPC 3 - Adivinha o Número?!
import random
n = random.randrange(1,101)
x = 0
superior = 100
inferior = 0
tentativas = 0


print ("Que jogo quer jogar?")

print("1-Adivinha o número que o computador está a pensar;") 
print("2-O computador adivinha o número que está a pensar")
jogo = int(input("Qual deles?"))

if jogo == 1:
    print ("Adivinhe o número que o computador está a pensar")
    tentativas = 100
    for total_tentativas in range(1, tentativas + 1):
        numero_str = input("Escreva um número: ")
        numero = int(numero_str)
        if numero < 1 or numero > 100:
            print ("Número inválido, o número tem que ser entre 1 e 100")
            continue
        acertou = numero == n
        maior = numero > n
        menor = numero < n
        if acertou:
            print (f"Acertou o número secreto em {total_tentativas} tentativas ^-^")
            break
        else:
            if maior:
                print("Escreva um número menor")
            elif menor:
                print("Escreva um numero maior")
    print ("Fim do Jogo")
elif jogo == 2:
    print (" Vou adivinhar o número em que está a pensar")
    tentativas = 100
    for total_tentativas in range(1, tentativas + 1):
        x = int((superior + inferior) / 2)
        resposta_str =input (f"O seu número é {x}? (Digite sim ou não)")
        if resposta_str == "sim":
            print(f"Acertei o número em {total_tentativas} tentativas ^-^")
            break
        else:
            resposta2_str = input ("É maior ou menor?")
            if resposta2_str == "maior":
                inferior = x
            else:
                superior = x
    print("Fim do Jogo")
