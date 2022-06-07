# opcoes = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]
import random

opcoes = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]

def jogar():
    print("Bem vindo ao jogo de Pedra, Papel, Tesoura, Lagarto e Spock")
    print("Escolha um dos itens abaixo:")
    for i in range(len(opcoes)):
        print(f"{i+1} - {opcoes[i]}")


    escolha_do_usuario = int(input("Qual é a sua escolha? "))
    escolha = opcoes[escolha_do_usuario - 1]
    escolha_do_computador = random.randint(0, len(opcoes)-1)
    print(f"você escolheu {escolha}")
    print(f"O computador escolheu {opcoes[escolha_do_computador]}")
    print(verificar_vencedor(escolha, opcoes[escolha_do_computador]))


def verificar_vencedor(escolha, escolha_do_computador):
    match escolha_do_computador:
        case "Pedra":
            if escolha == "Pedra":
                return "Empate"
            if escolha == "Papel":
                return "Você ganhou"
            if escolha == "Tesoura":
                return "Você perdeu"
            if escolha == "Lagarto":
                return "Você ganhou"
            if escolha == "Spock":
                return "Você perdeu"
        
        case "Papel":
            if escolha == "Pedra":
                return "Você perdeu"
            if escolha == "Papel":
                return "Empate"
            if escolha == "Tesoura":
                return "Você ganhou"
            if escolha == "Lagarto":
                return "Você perdeu"
            if escolha == "Spock":
                return "Você ganhou"
        
        case "Tesoura":
            if escolha == "Pedra":
                return "Você ganhou"
            if escolha == "Papel":
                return "Você perdeu"
            if escolha == "Tesoura":
                return "Empate"
            if escolha == "Lagarto":
                return "Você ganhou"
            if escolha == "Spock":
                return "Você perdeu"
            
        case "Lagarto":
            if escolha == "Pedra":
                return "Você perdeu"
            if escolha == "Papel":
                return "Você ganhou"
            if escolha == "Tesoura":
                return "Você perdeu"
            if escolha == "Lagarto":
                return "Empate"
            if escolha == "Spock":
                return "Você ganhou"

        case "Spock":
            if escolha == "Pedra":
                return "Você ganhou"
            if escolha == "Papel":
                return "Você perdeu"
            if escolha == "Tesoura":
                return "Você ganhou"
            if escolha == "Lagarto":
                return "Você perdeu"
            if escolha == "Spock":
                return "Empate"
    
jogar()

# Gabriel Henrique
# Mahiny Andrade
# Isabela Spirlandeli
# Diego Brito
# Henrique Marinho 
# Maycon Romão

