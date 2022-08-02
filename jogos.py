import adivinhacao
import forca

def escolha_jogos():
    print("**********************************")
    print("***Bem vindo Escolha o seu jogo***")
    print("**********************************")
    print("")
    print("(1) Adivinhação")
    print("(2) Forca")
    print("")

    jogo = int(input("Escolha seu Jogo: "))

    if(jogo==1):
        print("Adivinhação")
        adivinhacao.jogar()
    elif(jogo==2):
        print("Forca")
        forca.jogar()
   
        

if(__name__ == "__main__"):
    escolha_jogos()
    