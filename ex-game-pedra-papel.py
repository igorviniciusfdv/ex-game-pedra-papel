print('\33[1;31m-\33[m' * 10)
print('\33[1;31mJOKENPO\33[m')
print('\33[1;31m-\33[m' * 10)
print('Vamos jogar Pedra, Papel e Tesoura?')
from random import randint
print('Escolha entre:')
print('''1 - Papel
2 - Pedra
3 - Tesoura''')
pc = randint(1, 3)
jogador = int(input('Pedra, Papel ou Tesoura? '))
from time import sleep
print('E o vencedor é...')
sleep(3)
if jogador == 1 and pc ==2:
    print('\33[4;36mPARABÉNS, VOCÊ VENCEU!!\33[m Eu escolhi Pedra.')
elif jogador == 1 and pc == 3:
    print('\33[4;36mVOCÊ PERDEU!\33[m A minha escolha foi Tesoura.')
elif jogador == 2 and pc == 1:
    print('\33[4;36mVOCÊ PERDEU!\33[m Eu escolhi Papel.')
elif jogador == 2 and pc == 3:
    print('\33[4;36mPARABÉNS, VOCÊ VENCEU!!\33[m Minha escolha foi Tesoura!')
elif jogador == 3 and pc == 1:
    print('\33[4;36mPARABÉNS, VOCÊ CONSEGUIU ME VENCER!!\33[m Eu escolhi Papel!')
elif jogador == 3 and pc == 2:
    print('\33[4;36mVOCÊ PERDEU! Minha escolha foi Pedra.\33[m')
elif jogador == 1 and pc == 1:
    print('\33[4;36mEMPATE!\33[m Vamos jogar novamente!!')
elif jogador == 2 and pc == 2:
    print('\33[4;36mEMPATE!\33[m Vamos jogar novamente!!')
elif jogador == 3 and pc == 3:
    print('\33[4;36mEMPATE!\33[m Vamos jogar novamente!!')
else:
    print('\33[1;30mOPÇÃO INVÁLIDA!\33[m Tente novamente')





