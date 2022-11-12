import random  # importa biblioteca de random
import time  # importa biblioteca de tempo

from colorama import Fore, Back, Style 

#ARMAZENAMENTO
stop = 'Y'
ponto_jogador = 0
ponto_maquina = 0

#função de tempo
def pausa():
    print(Fore.RESET + 'Processando...')
    time.sleep(1)

while stop == 'Y':
    maquina = random.randint(1,3)
    jogador = int(input(Fore.RESET + 'ESCOLHA: [1] - PEDRA, [2] - PAPEL, [3] - TESOURA\n'))
    pausa()
    if jogador == maquina:
        print(Fore.MAGENTA + 'EMPATE')
    else:
        if jogador == 1:
            if maquina == 2:
                print(Fore.RED + 'MAQUINA GANHOU, PAPEL VENCE PEDRA.')
                ponto_maquina += 1
            elif maquina == 3:
                print(Fore.GREEN + 'JOGADOR GANHOU! PEDRA VENCE TESOURA')
                ponto_jogador += 1
        
        elif jogador == 2:
            if maquina == 1:
                print(Fore.GREEN + 'JOGADOR GANHOU! PAPEL VENCE PEDRA')
                ponto_jogador += 1
            elif maquina == 3:
                print(Fore.RED + 'MAQUINA GANHOU, TESOURA VENCE PAPEL')
                ponto_maquina += 1

        elif jogador == 3:
            if maquina == 1:
                print(Fore.RED + 'MAQUINA GANHOU, PEDRA VENCE TESOURA')
                ponto_maquina += 1
            elif maquina == 2:
                print(Fore.GREEN + 'JOGADOR GANHOU! TESOURA VENCE PAPEL')
                ponto_jogador += 1 
    stop = input(Fore.RESET + 'Jogar Novamente?  [Y/N]: ')
    pausa()


print(f'Fim de jogo!\nO Jogador ganhou {ponto_jogador} vez(es).\nA Maquina ganhou {ponto_maquina} vez(es).')



