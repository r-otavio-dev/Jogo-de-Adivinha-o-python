import random
jogador1 = input("Digite seu nome: ")
print(f"Bem-vindo ao jogo de adivinhação, {jogador1}!")
jogador2 = input("Digite o nome do seu amigo para jogar com você: ")
print(f"Olá, {jogador2}! Vamos começar o jogo de adivinhação!")

numero_secreto = random.randint(0, 50)

print(f"o jogador que ira começar será definido aleatoriamente... aguarde um momento...")
print(f"O jogador selecionado para começar é... {random.choice([jogador1, jogador2])}!")

print("O número secreto foi escolhido. Agora, cada jogador deve tentar adivinhar o número entre 0 e 50.")

print("O primeiro jogador a adivinhar o número secreto ganha o jogo!")

respostas = {jogador1: None, jogador2: None}

for rodada in range(1, 10000):
    for jogador in [jogador1, jogador2]:
        resposta = int(input(f"{jogador}, digite sua tentativa: "))
        respostas[jogador] = resposta
        
        if resposta == numero_secreto:
            print(f"Parabéns, {jogador}! Você adivinhou o número secreto e venceu o jogo!")
            exit()
        elif resposta < numero_secreto:
            print("O número secreto é maior do que sua tentativa.")
        else:
            print("O número secreto é menor do que sua tentativa.")