import pygame
import time

"""
    :param pontos_p1: numero de pontos do player 1 para serem expostos no placar
    :param pontos_p2: numero de pontos do player 2 para serem expostos no placar
    :return: void
"""

def placar(pontos_p1, pontos_p2):
    for i in range(2):
        for j in range(2):  # quadriculado placar
            pygame.draw.rect(tela, aqua, ((11 + i) * cell, (11 + j) * cell, cell, cell), 3)
    aux = 10
    txt_p1 = "P1"
    txt_p2 = "P2"
    txt_score_p1 = str(pontos_p1)
    txt_score_p2 = str(pontos_p2)

    fonte = pygame.font.SysFont("Comic Sams MS", 48)
    txt_1 = fonte.render(txt_p1, True, (0, 0, 0))
    txt_2 = fonte.render(txt_p2, True, (0, 0, 0))
    txt_3 = fonte.render(txt_score_p1, True, (0, 0, 0))
    txt_4 = fonte.render(txt_score_p2, True, (0, 0, 0))

    tela.blit(txt_1, ((11 * cell) + aux - 5, (11 * cell) + aux))
    tela.blit(txt_2, ((12 * cell) + aux - 5, (11 * cell) + aux))
    tela.blit(txt_3, ((11 * cell) + aux + 5, (12 * cell) + aux))
    tela.blit(txt_4, ((12 * cell) + aux + 5, (12 * cell) + aux))

    pygame.display.update()



def indicaTurno(player):
    """
    :param player: turno do jogador
    :return: void
    """
    if player == 1:

        pygame.draw.circle(tela, green, (cell * 10, cell * 12), 25, 0)
        pygame.draw.circle(tela, white, (cell * 14, cell * 12), 25, 0)

        pygame.display.update()

    elif player == 2:

        pygame.draw.circle(tela, white, (cell * 10, cell * 12), 25, 0)
        pygame.draw.circle(tela, green, (cell * 14, cell * 12), 25, 0)

        pygame.display.update()

def atualizaTelaCombate(matriz, jogador):

    """
    :param matriz: matriz de referencia
    :param jogador: jogador associado a matriz de referencia
    :return: void
    """

    """
    Essa funcao, basicamente, atualiza a tela do combate toda
    vez que é chamada, seja no turno do player 1 ou do player 2,
    quando eles fazem uma jogada (acertando barcos ou nao), a
    tela eh atualizada de acordo com o resultado da jogada.
    """
    if jogador == 1:
        for l in range(10):
            for c in range(10):
                if matriz[l][c] == 'O':

                    #Acertou barco

                    drawGroup = pygame.sprite.Group()
                    barco1 = pygame.sprite.Sprite(drawGroup)
                    explosion = pygame.sprite.Sprite(drawGroup)
                    explosion.image = pygame.image.load("imagens/explosion1.png")
                    barco1.image = pygame.image.load("imagens/barco_explodido-removebg-preview.png")
                    barco1.image = pygame.transform.scale(barco1.image, [60, 48])  # (135, 50)
                    barco1.rect = pygame.Rect(((c + 1) * cell, (l + 1) * cell, cell, cell))
                    explosion.rect = pygame.Rect(((c + 1) * cell, (l + 1) * cell, cell, cell))
                    explosion.image = pygame.transform.scale(explosion.image, [60, 48])  # (135, 50)
                    drawGroup.draw(tela)
                    pygame.display.update()


                if matriz[l][c] == 'X':

                    #acertou agua

                    drawGroup = pygame.sprite.Group()
                    agua = pygame.sprite.Sprite(drawGroup)
                    bomb = pygame.sprite.Sprite(drawGroup)
                    bomb.image = pygame.image.load("imagens/sea_mine_02.png")
                    agua.image = pygame.image.load("imagens/Blue Ring Explosion9.png")
                    agua.image = pygame.transform.scale(agua.image, [60, 48])  # (135, 50)
                    agua.rect = pygame.Rect((c + 1) * cell, (l + 1) * cell, cell, cell)
                    bomb.rect = pygame.Rect((c + 1) * cell + 8, (l + 1) * cell + 8, cell, cell)
                    drawGroup.draw(tela)
                    pygame.display.update()


    else:
        for l in range(10):
            for c in range(10):
                if matriz[l][c] == 'O':

                    #acertou barco

                    drawGroup = pygame.sprite.Group()
                    barco1 = pygame.sprite.Sprite(drawGroup)
                    explosion = pygame.sprite.Sprite(drawGroup)
                    explosion.image = pygame.image.load("imagens/explosion1.png")
                    barco1.image = pygame.image.load("imagens/barco_explodido-removebg-preview.png")
                    barco1.image = pygame.transform.scale(barco1.image, [60, 48])  # (135, 50)
                    barco1.rect = pygame.Rect(((c + 13) * cell, (l + 1) * cell, cell, cell))
                    explosion.rect = pygame.Rect(((c + 13) * cell, (l + 1) * cell, cell, cell))
                    explosion.image = pygame.transform.scale(explosion.image, [60, 48])
                    drawGroup.draw(tela)
                    pygame.display.update()


                if matriz[l][c] == 'X':

                    #acertou agua

                    drawGroup = pygame.sprite.Group()
                    agua = pygame.sprite.Sprite(drawGroup)
                    bomb = pygame.sprite.Sprite(drawGroup)
                    bomb.image = pygame.image.load("imagens/sea_mine_02.png")
                    agua.image = pygame.image.load("imagens/Blue Ring Explosion9.png")
                    agua.image = pygame.transform.scale(agua.image, [60, 48])  # (135, 50)
                    agua.rect = pygame.Rect((c + 13) * cell, (l + 1) * cell, cell, cell)
                    bomb.rect = pygame.Rect((c + 13) * cell + 8, (l + 1) * cell + 8, cell, cell)
                    drawGroup.draw(tela)
                    pygame.display.update()

    pygame.display.update()


def criaMatriz(m , l, c):

    """
    :param m: matriz de referencia
    :param l: linhas da matriz
    :param c: colunas da matriz
    :return:
    """
    #cria uma matriz l x c a partir de uma matriz m vazia
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(' ')
        m.append(linha)


def addBarcos(x, y, matriz, tam, num, simb):

    """
    :param x: coordenada x do cursor

    :param y: coordenada y do cursor

    :param matriz: matriz a qual terá o seu barco adicionado

    :param tam: tamanho do barco

    :param num: numero de barcos a serem adicionados

    :param simb: character o qual será utilizado pra simbolizar o barco
    dentro da matriz a qual a função está interagindo

    :return:
    retorna 1 quando há sobreposicao dos barcos.
    retorna 0 caso a coordenada passada pelo cursor do usuário seja invalida.
    (fora do quadrado pra adicionar os barcos).
    retorn 2 quando o barco é adicionado com sucesso na matriz de referencia.

    """

    barcos_tot = 0
    letra = chr(simb)

    # adiciona barcos ate o limite num
    while num > barcos_tot:

        while True:

            sobreposicao = False

            # Condicao que garante que as coordenadas inseridas sejam
            # validas, ou seja, nao ultrapassa os limites.
            if (10 - tam) >= x >= 0 and 9 >= y >= 0:
                for cont in range(tam):
                    # Testa se ha sobreposicao
                    if matriz[y][x + cont] != ' ':
                        sobreposicao = True

                if sobreposicao == False:
                    break

                else:
                    sobreposicao = False
                    return 1
            else:
                return 0

        # Adiciona os barcos na matriz e fazendo a diferenciacao
        # de cada barco (barco 1 = A, barco 2 = B, barco 3 = C ...)
        for cont in range(tam):
            #guarda a posicao do barco na matriz
            matriz[y][x + cont] = letra
            #pinta a tela na coordenada especifica do clique do cursor.

            drawGroup = pygame.sprite.Group()
            barco = pygame.sprite.Sprite(drawGroup)
            barco.image = pygame.image.load("imagens/barcoo.png")
            barco.image = pygame.transform.scale(barco.image, [140, 48])    #(135, 50)
            barco.rect = pygame.Rect(((x + 7) * cell, (y + 1) * cell, cell, cell))
            drawGroup.draw(tela)


            pygame.display.update()
        barcos_tot += 1

    return 2


def combateNaval(cord_x, cord_y, m1, m2, m1_aux, m2_aux, player):

    """

    :param x: coordenada x do cursor

    :param y: coordenada y do cursor

    :param m1: matriz do jogador 1

    :param m2: matriz do jogador 2

    :param m1_aux: matriz que o jogador 2 ataca

    :param m2_aux: matriz que o jogador 1 ataca

    :param player: turno do jogador atual.

    :return:

    retorna 3 quando as coordenadas passadas pelo usuário são invalidas.
    retorna 1 quando o 'player 1' atinge um dos barcos do 'player 2'.
    retorna 2 quando o 'player 2' atinge um dos barcos do 'player 1'.
    retorna 0 quando o 'player 1' ou 'player 2' não atingem nenhum barco,
    atingem o mar.

    """

    indicaTurno(player)

    while True:

        while 1:

            if player == 1: #player

                #Testa a validade do tiro, ou seja, se o tiro
                #foi dado em algum espaco valido.
                #(Coordenadas adaptadas para cada player)

                if 10 > cord_x >= 0 and 10 > cord_y >= 0 and m2_aux[cord_y][cord_x] == ' ':
                    break
                else:
                    indicaTurno(player)
                    atualizaTelaCombate(m1_aux, 2)
                    atualizaTelaCombate(m2_aux, 1)
                    return 3

            elif player == 2: #player2
                if 22 > cord_x >= 12 and 10 > cord_y >= 0 and m1_aux[cord_y][cord_x - 12] == ' ':
                    break
                else:
                    indicaTurno(player)
                    atualizaTelaCombate(m1_aux, 2)
                    atualizaTelaCombate(m2_aux, 1)
                    return 3


        if player == 1: #player 1

            #Acertou um barco do player 2
            if m2[cord_y][cord_x] != ' ' and m2[cord_y][cord_x] != 'X':
                barco = m2[cord_y][cord_x]
                for i in range(10):
                    for j in range(10):
                        if m2[i][j] == barco:
                            m2_aux[i][j] = 'O'

                atualizaTelaCombate(m1_aux, 2)
                atualizaTelaCombate(m2_aux, 1)

                pygame.display.update()

                bomb_ship.play()

                return 1

            #Acertou a água do player 2
            elif m2[cord_y][cord_x] == ' ':
                m2_aux[cord_y][cord_x] = 'X'

                atualizaTelaCombate(m1_aux, 2)
                atualizaTelaCombate(m2_aux, 1)

                bomb_water.play()

                pygame.display.update()

                return 0


        elif player == 2: #player 2

            # Acertou um barco do player 1
            if m1[cord_y][cord_x - 12] != ' ' and m1[cord_y][cord_x - 12] != 'X':
                barco = m1[cord_y][cord_x - 12]
                for i in range(10):
                    for j in range(10):
                        if m1[i][j] == barco:
                            m1_aux[i][j] = 'O'

                            atualizaTelaCombate(m1_aux, 2)
                            atualizaTelaCombate(m2_aux, 1)

                            bomb_ship.play()

                pygame.display.update()

                return 2

            # Acertou a água do player 1
            elif m1[cord_y][cord_x - 12] == ' ':
                m1_aux[cord_y][cord_x - 12] = 'X'

                atualizaTelaCombate(m1_aux, 2)
                atualizaTelaCombate(m2_aux, 1)

                bomb_water.play()

                pygame.display.update()

                return 0


#PROGRAMA PRINCIAL

#inicializa o pygame
pygame.init()

# ------- DEFINICAO DE VARIAVEIS -------

white = (255, 255,255)
azul_claro = (100, 149, 237)
cinza = (128, 128, 128)
black = (0, 0, 0)
red = (205, 0, 0)
green = (50,205,50)
gainsboro = (211, 211, 211)
aqua = (135,206,250)

cell = 50
num_l = 10 #linhas
num_c = 10 #colunas

"""
Player 1 ataca a 'matriz_combate_p2' usando como referencia a 'matriz_play_2'
Player 2 ataca a 'matriz_combate_p1' usando como referencia a 'matriz_play_1'
"""

matriz_play_1 = []
matriz_play_2 = []
matriz_combate_p1 = []
matriz_combate_p1_aux = []
matriz_combate_p2 = []
matriz_combate_p2_aux = []

criaMatriz(matriz_play_1, 10, 10)
criaMatriz(matriz_play_2, 10, 10)
criaMatriz(matriz_combate_p1, 10, 10)
criaMatriz(matriz_combate_p2, 10, 10)
criaMatriz(matriz_combate_p1_aux, 10, 10)
criaMatriz(matriz_combate_p2_aux, 10, 10)

aux = 0
char = 65
tot_barcos = 7
barcos_p1 = 0
barcos_p2 = 0
combate = False
turno = 1
intervalo = True
res = 0
cont = 0
pontos_p1 = 0
pontos_p2 = 0

#garantir que a condicao de inicio seja aplicada somente uma vez
comecou = False
jogo = True

# ------- FIM DA DEFINICAO DE VARIAVEIS -------

# TELA INICIAL DO JOGO
tela = pygame.display.set_mode((24 * cell, 14 * cell), 0, 32)
pygame.display.set_caption("BATALHA NAVAL")

drawGroup = pygame.sprite.Group()
fundo = pygame.sprite.Sprite(drawGroup)
fundo.image = pygame.image.load("imagens/fundo-azul-png.png")
fundo.rect = pygame.Rect(0, 0, 0, 0)

tela.fill(azul_claro)
drawGroup.draw(tela)
pygame.display.update()


#carregando imagens da tela inicial

'''
Utlização do drawGroup ao longo do código  para a junção dos elementos
Aqui, como também em partes posterioremos, utilizamos o Sprite para carregar imagens diversas e o .rect para ajustar
a localização da imagem no display
'''

drawGroup = pygame.sprite.Group()
mar = pygame.sprite.Sprite(drawGroup)
logo = pygame.sprite.Sprite(drawGroup)
barco = pygame.sprite.Sprite(drawGroup)
nuvem = pygame.sprite.Sprite(drawGroup)

logo.image = pygame.image.load("imagens/logo1.png")
logo.rect = pygame.Rect(342, -90, 300, -10)
mar.image = pygame.image.load("imagens/onda2.png")
mar.rect = pygame.Rect(-200, 0, 10, 0)
barco.image = pygame.image.load("imagens/barco4.png")
barco.rect = pygame.Rect(-10, 40, 0, 0)
barco.image = pygame.transform.scale(barco.image, [450, 300])
nuvem.image = pygame.image.load("imagens/nuvem.png")
nuvem.rect = pygame.Rect(910, 60, -142, -100)

#efeitos sonoros

bomb_ship = pygame.mixer.Sound("sons/explosion09.wav")
bomb_water = pygame.mixer.Sound("sons/watersplash2.flac")


#musica da tela inicial

pygame.mixer.music.load("sons/musica_inicial.mp3")
pygame.mixer.music.play(-1)


pygame.draw.rect(tela, black, (400, 350, 400, 100), 3) #Play
pygame.draw.rect(tela, black, (400, 500,  400, 100), 3) #Quit
tela.fill(white, (400, 350, 400, 100))
tela.fill(white, (400, 500, 400, 100))


drawGroup.draw(tela)

txt_start = "START"
txt_exit = "EXIT"
fonte = pygame.font.SysFont("Comic Sams MS", 48)
txt_1 = fonte.render(txt_start, True, (0, 0, 0))
txt_2 = fonte.render(txt_exit, True, (0, 0, 0))

tela.blit(txt_1, (150 + 400, 375))
tela.blit(txt_2, (160 + 400, 525))

pygame.display.update()


while jogo:


    for evento in pygame.event.get():

        # Evento que fecha a janela
        if (evento.type == pygame.QUIT):
            jogo = False

        #comeca o jogo

        if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
            # Pega as coordenadas do ponto de clique e calcula a celula

            # Captura as posicoes do cursor.
            mouse_x, mouse_y = evento.pos
            # print(f"x = {mouse_x}, y = {mouse_y}")
            celula_x = (mouse_x // cell) - 1
            celula_y = (mouse_y // cell) - 1

            print(f'posicao: ({celula_x}, {celula_y})')

            # preencher embarcacoes #player 1
            if comecou and 15 >= celula_x >= 6 and 9 >= celula_y >= 0 and barcos_p1 < tot_barcos:
                if addBarcos(celula_x - 6, celula_y, matriz_play_1, 3, 1, char) <= 1:
                    pass
                else:
                    char += 1
                    barcos_p1 += 1
                    if barcos_p1 == tot_barcos:
                        time.sleep(1)

            # preencher embarcacoes #player 2
            if 15 >= celula_x >= 6 and 9 >= celula_y >= 0 and barcos_p2 < tot_barcos and barcos_p1 > tot_barcos:
                if addBarcos(celula_x - 6, celula_y, matriz_play_2, 3, 1, char) <= 1:
                    pass
                else:
                    char += 1
                    barcos_p2 += 1
                    if barcos_p2 == tot_barcos:
                        time.sleep(1)
                        combate = True

            if barcos_p1 == tot_barcos:

                # imagens da tela de preenchimento do player 2
                drawGroup = pygame.sprite.Group()
                moldura = pygame.sprite.Sprite(drawGroup)
                moldura.image = pygame.image.load("imagens/b.png")
                moldura.image = pygame.transform.scale(moldura.image, [1199, 694])  #alterando a resolução da imagem
                moldura.rect = pygame.Rect(0, 0, 100, 1000) #alterando a posição da imagem
                tela.fill(azul_claro)

                drawGroup.draw(tela)

                pygame.display.update()
                time.sleep(2)
                tela.fill(azul_claro)

                # imagens da tela do turno do player 2
                drawGroup = pygame.sprite.Group()
                moldura = pygame.sprite.Sprite(drawGroup)
                moldura.image = pygame.image.load("imagens/plano_player2.png")
                moldura.rect = pygame.Rect(0, 0, 0, 0)  #imagem da tela centralizada no fundo

                tela.fill(azul_claro)
                drawGroup.draw(tela)


                for i in range(0, num_l):
                    for j in range(0, num_c): #quadriculado
                        pygame.draw.rect(tela, white, ((7 + i) * cell, (1 + j) * cell, cell, cell), 3)

                pygame.display.update()
                pygame.display.update()
                barcos_p1 += 1

            #Clique Start => Começar a partida
            if 6 < celula_x <= 14 and 6 <= celula_y <= 7 and aux == 0:

                # imagens da tela de preenchimento do player 1
                drawGroup = pygame.sprite.Group()
                fundo = pygame.sprite.Sprite(drawGroup)
                fundo.image = pygame.image.load("imagens/background1.png")
                fundo.image = pygame.transform.scale(fundo.image, [1200, 712])  #alteando a resolução da imagem
                fundo.rect = pygame.Rect(0, -14, 100, 1000)
                tela.fill(white)
                drawGroup.draw(tela)

                pygame.display.update()
                time.sleep(4)
                aux = 1

                # imagens da tela do turno do player 1
                drawGroup = pygame.sprite.Group()
                moldura = pygame.sprite.Sprite(drawGroup)
                moldura.image = pygame.image.load("imagens/plano1.png")
                moldura.rect = pygame.Rect(0, 0, 0, 0)
                tela.fill(azul_claro)
                drawGroup.draw(tela)

                for i in range(0, num_l):
                    for j in range(0, num_c):    #quadriculado
                        pygame.draw.rect(tela, white, ((7 + i) * cell, (1 + j) * cell, cell, cell), 3)

                pygame.display.update()

                pygame.display.update()
                comecou = True



            #Clique Exit => Fechar o jogo
            if 6 < celula_x <= 14 and 9 <= celula_y <= 10 and aux == 0:
                jogo = False

            #COMBATE JOGADOR 1 VS JOGADOR 2
            if barcos_p1 >= 5 and barcos_p2 >= 5 and combate:

                if intervalo:
                    # imagem da tela inicial de combate
                    drawGroup = pygame.sprite.Group()
                    fundo = pygame.sprite.Sprite(drawGroup)
                    fundo.image = pygame.image.load("imagens/combate1.png")
                    fundo.rect = pygame.Rect(0, 0, 0, 0)
                    tela.fill(azul_claro)
                    drawGroup.draw(tela)

                    pygame.display.update()
                    pygame.mixer.music.load("sons/battleThemeA.mp3")  #utilizando o mixer para reprodução da música ao fundo
                    pygame.mixer.music.play(-1)  #-1 é indicativo para a música tocar em looping
                    time.sleep(3)
                    tela.fill(azul_claro)
                    intervalo = False

                drawGroup = pygame.sprite.Group()
                oceano = pygame.sprite.Sprite(drawGroup)
                oceano.image = pygame.image.load("imagens/telao.png")
                oceano.rect = pygame.Rect(0, 0, 0, 0)
                tela.fill(azul_claro)
                drawGroup.draw(tela)

                for i in range(0, num_l):
                    for j in range(0, num_c):  # quadriculado p1
                        pygame.draw.rect(tela, white, ((1 + i) * cell, (1 + j) * cell, cell, cell), 3)

                for i in range(0, num_l):
                    for j in range(0, num_c):  # quadriculado p2
                        pygame.draw.rect(tela, white, ((13 + i) * cell, (1 + j) * cell, cell, cell), 3)

                pygame.display.update()

                if cont == 0:
                    indicaTurno(1)
                pygame.display.update()

                for i in range(0, num_l):
                    for j in range(0, num_c):
                        matriz_combate_p1_aux[i][j] = matriz_combate_p1[i][j]
                        matriz_combate_p2_aux[i][j] = matriz_combate_p2[i][j]


                if cont > 0:
                    res = combateNaval(celula_x, celula_y, matriz_play_1, matriz_play_2, matriz_combate_p1,
                                       matriz_combate_p2, turno)
                cont += 1

                if   res == 1:
                    pontos_p1 += 1
                elif res == 2:
                    pontos_p2 += 1

                for i in range(0, num_l):
                    for j in range(0, num_c):
                        if matriz_combate_p1_aux[i][j] != matriz_combate_p1[i][j]:
                            turno = 1

                        if matriz_combate_p2_aux[i][j] != matriz_combate_p2[i][j]:
                            turno = 2

                indicaTurno(turno)
                placar(pontos_p1, pontos_p2)

                if pontos_p1 == 7:

                    time.sleep(2)
                    drawGroup = pygame.sprite.Group()
                    jogador1 = pygame.sprite.Sprite(drawGroup)
                    jogador1.image = pygame.image.load("imagens/one.png")
                    jogador1.rect = pygame.Rect(0, 0, 0, 0)
                    drawGroup.draw(tela)

                    pygame.mixer.music.load("sons/Can't Stop Winning MP3.mp3")  #carregando do som da dela final
                    pygame.mixer.music.play(1)

                    pygame.display.update()
                    time.sleep(30)
                    jogo = False

                elif pontos_p2 == 7:

                    time.sleep(2)
                    drawGroup = pygame.sprite.Group()
                    jogador2 = pygame.sprite.Sprite(drawGroup)
                    jogador2.image = pygame.image.load("imagens/twi.png")
                    jogador2.rect = pygame.Rect(0, 0, 0, 0)
                    drawGroup.draw(tela)

                    pygame.mixer.music.load("sons/Can't Stop Winning MP3.mp3")
                    pygame.mixer.music.play(1)

                    drawGroup.draw(tela)
                    pygame.display.update()
                    time.sleep(30)
                    jogo = False

pygame.display.update()

pygame.quit()
