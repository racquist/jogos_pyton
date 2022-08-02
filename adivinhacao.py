import random
import jogos

def jogar():

    mensagem_boas_vindas()
    numero_secreto = numero()
    total_de_tentativas= dificuldade_do_jogo()
   
    pontos =1000

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = chute_jogador()
        limite = valor_dentro_do_range(chute)

        if(not limite):
            continue
        else:        
            acertou = chute == numero_secreto
            maior = chute>numero_secreto
            menor = chute<numero_secreto

            if(acertou):
                print("Você Acertou e fez {} pontos".format(pontos))
                break
            else:
                if(maior):
                    print("Você Errou! O seu Chute foi maior que o numero secreto!")
                elif(menor):
                    print("Você Errou! O seu chute foi menor que o número secreto!")
                pontos = calcula_pontos(pontos, chute, numero_secreto)
    
    mensagem_final()
    

def mensagem_boas_vindas():
    print("**************************************")
    print("***Bem vindo ao jogo de Adivinhação***")
    print("**************************************")
    print("")

def numero():
    numero_secreto = random.randrange(1,101)
    return numero_secreto

def dificuldade_do_jogo():
    
    print("Escolha o nível de dificuldade:")
    nivel = int(input("(1)Fáci - (2)Médio - (3)Difícil: "))
    if(nivel==1):
        total_de_tentativas = 20
    elif(nivel==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    return total_de_tentativas

def chute_jogador():
    chute = int(input("Digite um número entre 1 e 100 "))
    print("Você digitou: " , chute)
    return chute

def valor_dentro_do_range(chute):
    if(chute<1 or chute>100):
        print("Número fora do Range! você perdeu esta rodada!")
        limite = False
    else:
        limite = True

    return limite    

def calcula_pontos(pontos, chute, numero_secreto):
    pontos_perdidos = abs(chute - numero_secreto)
    pontos -= pontos_perdidos
    return pontos

def mensagem_final():
    print("Fim do Jogo")
    jogos.escolha_jogos()

if(__name__ == "__main__"):
    jogar()