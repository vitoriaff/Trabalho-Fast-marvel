
import random
import time
import numpy
opcN = None
opcJ = None
listaNome=["Capitao America","Thor","Hulk","Homem de Ferro","Capita Marvel","Viuva Negra","Wanda","Visao","Pantera Negra","Homem Formiga","Homem Aranha","Thanos","Doutor Estranho","Gaviao Arqueiro","Loki","Gamora","Groot","Vespa","Falcao","Soldado Invernal","Mercurio","Rocky","Nebulosa"] 
def sortearNome(_listaNome):
  j = len(_listaNome)
  i = random.randint(1,j)
  index = 0
  while (index < 1):
    nome = _listaNome[i-1]
    index += 1
  return nome

while True:
  print('-------------------------------------------------------------------------')
  print('   ⍟                     JOGO FAST MARVEL                        ✵     ')
  print('                  ۞          MENU :                       ४             ')
  print('                                              ⎊                          ') 
  print('  ᗢ                       Opção 1: jogar                                ✪')
  print('        ✇                 Opção 2: Opções             ϟ                  ')
  print('                  ꘩       Opção 3: Sair                            ⧗     ')
  print('-------------------------------------------------------------------------')
  print(' ')
  opcao = int(input('     Ⓐ            Qual é a opção escolhida:     ➳ '))
  print(' ')
  if (opcao > 3 or opcao <1):
    print('                   Favor escolha entre corretamente')
    print(' ')
  elif (opcao ==1):
    if (opcJ == None or opcN == None):
      print('                  Favor escolha as opçoes de jogo antes de iniciar o game')
      print(' ')
    else:
      if (opcJ == 2):
        jogador1 = input('      ◊             Escreva o nome do jogador 1:  ')
        jogador2 = input('               ➃    Escreva o nome do jogador 2:  ')
        print('---------------------------------------------------------------------------')
        index = 0
        #Loop para fazer o random dos nomes
        if (jogador1 != None):
          tempo_jogador1 = time.time()
          while True:
            if (index == opcN):
              tempo2_jogador1 = time.time()
              tempoFinalJogador1 = tempo2_jogador1 - tempo_jogador1
              print(f'                          {jogador1} seu tempo foi de: {tempoFinalJogador1: .2f}')
              break
            nome = sortearNome(listaNome)
            nomeComparativo = input(f'                Escreve {nome} corretamente: ')
            print('---------------------------------------------------------------------------')
            while True:
              if (nome == nomeComparativo):
                break
              else:
                print('                                   Você errou')
                nomeComparativo = input(f'                Escreve {nome} corretamente: ')
                print('---------------------------------------------------------------------------')
            index +=1
        if (jogador2 != None):
          print(f'\n                              {jogador2} Seu jogo vai começar')
          tempo_jogador2 = time.time()
          index = 0
          while True:
            tempo_espera = time.time()
            espera = tempo_espera - tempo_jogador2
            if (espera == 2):
              print(f'                             {jogador2} seu jogo começou!')
              print('---------------------------------------------------------------------------')
              tempo_jogador2 = time.time()
              break
          while True:
            if (index == opcN):
              tempo2_jogador2 = time.time()
              tempoFinalJogador2 = tempo2_jogador2 - tempo_jogador2
              print(f'                                    {jogador2} seu tempo foi de: {tempoFinalJogador2: .2f}')
              break
            nome = sortearNome(listaNome)
            nomeComparativo = input(f'                    Escreve {nome} corretamente: ')
            while True:
              if (nome == nomeComparativo):
                break
              else:
                nomeComparativo = input(f'                 Escreve {nome} corretamente: ')
            index +=1
        if (tempoFinalJogador2 > tempoFinalJogador1):
          print(f'        Parabens {jogador2} vc venceu e seu tempo foi de: {tempoFinalJogador2: 2.f} contra {tempoFinalJogador1: 2.f}s do {jogador1}')
        if (tempoFinalJogador2 < tempoFinalJogador1):
          print(f'        Parabens {jogador1} vc venceu e seu tempo foi de: {tempoFinalJogador1: 2.f} contra {tempoFinalJogador2: 2.f}s do {jogador2}')
      if (opcJ == 3):
        jogador1 = input('               Escreva o nome do jogador 1: ')
        jogador2 = input('               Escreva o nome do jogador 2: ')
        jogador3 = input('               Escreva o nome do jogador 3: ')
        print('---------------------------------------------------------------------------')
        index = 0
        #Loop para fazer o random dos nomes
        if (jogador1 != None):
          tempo_jogador1 = time.time()
          while True:
            if (index == opcN):
              tempo2_jogador1 = time.time()
              tempoFinalJogador1 = tempo2_jogador1 - tempo_jogador1
              print(f'                       {jogador1} seu tempo foi de: {tempoFinalJogador1: .2f}')
              break
            nome = sortearNome(listaNome)
            nomeComparativo = input(f'                Escreve {nome} corretamente: ')
            while True:
              if (nome == nomeComparativo):
                break
              else:
                nomeComparativo = input(f'               Escreve {nome} corretamente: ')
            index +=1
        if (jogador2 != None):
          print(f'\n                                    {jogador2} Seu jogo vai começar')
          index = 0
          tempo_jogador2 = time.time()
          while True:
            tempo_espera = time.time()
            espera = tempo_espera - tempo_jogador2
            if (espera == 2):
              print(f'                                    {jogador2} seu jogo começou!')
              tempo_jogador2 = time.time()
              break
          while True:
            if (index == opcN):
              tempo2_jogador2 = time.time()
              tempoFinalJogador2 = tempo2_jogador2 - tempo_jogador2
              print(f'                                {jogador2} seu tempo foi de: {tempoFinalJogador2: .2f}')
              break
            nome = sortearNome(listaNome)
            nomeComparativo = input(f'               Escreve {nome} corretamente: ')
            while True:
              if (nome == nomeComparativo):
                break
              else:
                nomeComparativo = input(f'               Escreve {nome} corretamente: ')
            index +=1
        if (jogador3 != None):
          print(f'\n                                    {jogador3} Seu jogo vai começar')
          index = 0
          tempo_jogador3 = time.time()
          while True:
            tempo_espera = time.time()
            espera = tempo_espera - tempo_jogador3
            if (espera == 2):
              print(f'                                     {jogador3} seu jogo começou!')
              tempo_jogador3 = time.time()
              break
          while True:
            if (index == opcN):
              tempo2_jogador3 = time.time()
              tempoFinalJogador3 = tempo2_jogador3 - tempo_jogador3
              print(f'                         {jogador3} seu tempo foi de: {tempoFinalJogador3: .2f}')
              break
            nome = sortearNome(listaNome)
            nomeComparativo = input(f'               Escreve {nome} corretamente: ')
            while True:
              if (nome == nomeComparativo):
                break
              else:
                nomeComparativo = input(f'               Escreve {nome} corretamente: ')
            index +=1
  elif (opcao == 2):
    while True:
      opc = int(input('       Escolha 1: para escolher a quantidade de jogadores \n       Escolha 2: para escolher a quantidade de nomes sorteados: '))
      print('-------------------------------------------------------------------------')
      if (opc > 2 or opc < 1):
        print('                    Favor digite conforme o menu')
        print('-------------------------------------------------------------------------')
      elif (opc == 1):
        opcJ = int(input('                  Escolha entre 2 a 3 jogadores: '))
        if (opcJ < 2 or opcJ>3):
          print('                             Favor escolha ente 2 a 3 jogadores')
        else:
          break
      elif (opc == 2):
        opcN = int(input('       Escolha a quantidade de nomes que serão sorteados entre 5 a 10: '))
        if (opcN>10 or opcN<5):
          print('                              Favor escolha entre 5 a 10')
        else:
          break
  elif (opcao ==3):
    print('               Obrigado por jogar nosso jogo até a proxima')
    break1
