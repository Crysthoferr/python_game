import random
from time import sleep
print('\033[0;31m-=-=-=-=-=\033[m JOKENPÔ \033[0;31m-=-=-=-=-=\033[m')
print('\033[0;31m|\033[m Suas opções:              \033[0;31m|\033[m')
print('\033[0;31m|\033[m \033[0;32m[1] PEDRA\033[m                 \033[0;31m|\033[m')
print('\033[0;31m|\033[m \033[0;32m[2] PAPEL\033[m                 \033[0;31m|\033[m')
print('\033[0;31m|\033[m \033[0;32m[3] TESOURA\033[m               \033[0;31m|\033[m')
print('\033[0;31m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
while True:
    opcao = int(input('Qual a sua jogada?(\033[0;31mAPENAS NÚMEROS!\033[m) '))
    print('\033[0;31m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m')
    if opcao == 1:
        usuario = 'PEDRA'
        print(f' Você escolheu {usuario}')
        break
    elif opcao == 2:
        usuario = 'PAPEL'
        print(f' Você escolheu {usuario}')
        break
    elif opcao == 3:
        usuario = 'TESOURA'
        print(f' Você escolheu {usuario}')
        break
    else:
        print('Valor inválido..tente novamente')   
res = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.choice(res)
print(f' O computador escolheu {computador}')
print('\033[0;31m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m')
print('\033[0;34mJO\033[m')
sleep(1)
print('\033[0;34mKEN\033[m')
sleep(1)
print('\033[0;34mPÔ\033[m')
sleep(2)
if usuario == computador:
    print('EMPATE...Tente novamente')
elif usuario == 'PAPEL' and computador == 'PEDRA':
    print('\033[0;32mVocê VENCEU!\033[m')
elif usuario == 'PAPEL' and computador == 'TESOURA':
    print('\033[0;31mVocê PERDEU! Tente novamente...\033[m')
elif usuario == 'TESOURA' and computador == 'PAPEL':
    print('\033[0;32mVocê VENCEU!\033[m')
elif usuario == 'TESOURA' and computador == 'PEDRA':
    print('\033[0;31mVocê PERDEU! Tente novamente...\033[m')
elif usuario == 'PEDRA' and computador == 'TESOURA':
    print('\033[0;32mVocê VENCEU!\033[m')
elif usuario == 'PEDRA' and computador == 'PAPEL':
    print('\033[0;31mVocê PERDEU! Tente novamente...\033[m')
else:
    print('Digite um comando válido!')
