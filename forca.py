import random
import jogos

def jogar():
    mensagem_de_boas_vindas()
    palavra_secreta = define_palavra_secreta()
    letras_certas = inicializa_letras_certas(palavra_secreta)
    print(letras_certas)
        
    erros = 0
    enforcou = False
    acertou = False
    

    while(not enforcou and not acertou):
        
        chute = recebe_chute_jogador()

        if(chute in palavra_secreta):
            preenche_palavra(chute, palavra_secreta, letras_certas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_certas
        print(letras_certas)
    
    mensagem_final(acertou)

def mensagem_de_boas_vindas():
    print("********************************")
    print("***Bem vindo ao jogo da Forca***")
    print("********************************")
    print("")
    
def tipo_palavra():    
    categoria = input("Qual categoria de palavra você prefere? (Frutas/Carros) ")
    categoria = categoria.strip()
    categoria = categoria.lower()
    return categoria   

def define_palavra_secreta():
    categoria = tipo_palavra()
    arquivo = open("C:/Users/ACR1JVL/Documents/Alura/Python/iniciando_Phyton/Jogos/{}.txt".format(categoria), "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_certas(palavra):
    return ["_" for letra in palavra]

def recebe_chute_jogador():
    chute = input("Digite uma letra: ")
    chute = chute.strip()
    chute = chute.upper()
    return chute

def preenche_palavra(chute, palavra_secreta, letras_certas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_certas[index] = letra            
        index += 1 

def mensagem_final(acertou):
    if(acertou):
        print("Você Ganhou!")
        resposta = input("Você pode adicionar uma palavra ao baco de dados, você quer fazer isso?(S/N) ")
        resposta = resposta.strip()
        resposta = resposta.upper()
        if (resposta == 'S'):
            adiciona_palavra()
    else:
        print("Você Perdeu!")
    print("fim de Jogo")
    jogos.escolha_jogos()

def adiciona_palavra():
    categoria = tipo_palavra()
    palavra = input("Digite sua palavra: ")
    palavra = palavra.strip()
    palavra = palavra.upper()
    arquivo = open("C:/Users/ACR1JVL/Documents/Alura/Python/iniciando_Phyton/Jogos/{}.txt".format(categoria), "a")
    arquivo.write('\n' + palavra)
    arquivo.close()
    print("Palavra adicionada com sucesso!")

if(__name__ == "__main__"):
    jogar()