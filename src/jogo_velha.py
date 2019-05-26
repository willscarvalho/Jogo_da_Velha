import pygame
from pygame.locals import *
from sys import exit

'''
    img_xR = pygame.transform.scale(img_x, (100, 100))
    img_oR = pygame.transform.scale(img_o, (100, 100))
    img_tR = pygame.transform.scale(img_t, (100, 100))
'''
def carregar_img_x():
    img_X = pygame.image.load('img/Red_Cross.png').convert_alpha()
    return img_X

def carregar_img_o():
    img_O = pygame.image.load('img/Circle.png').convert_alpha()
    return img_O

def criar_tabuleiro():
    """
    Função que cria o tabuleiro das posições do jogo.
    Return: retorno uma listas contendo outra 3 listas respectivamente
    com os valores vazio do tabuleiro -> representação de matriz em python.
    """
    tabuleiro = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
    return tabuleiro

def escolher_jogador(posicao, tela):
    x, y = posicao
    if vez == 'JOGADOR1':
        imgO = carregar_img_o()
        imgOR = pygame.transform.scale(imgO, (100, 100))
        tela.blit(imgOR, (x - 50, y - 50))
    else:
        imgX = carregar_img_x()
        imgXR = pygame.transform.scale(imgX, (100, 100))
        tela.blit(imgXR, (x - 50, y - 50))

def definir_rect():
    rect1 = Rect((0, 0), (200, 200))
    rect2 = Rect((200, 0), (200, 200))
    rect3 = Rect((400, 0), (200, 200))
    rect4 = Rect((0, 200), (200, 200))
    rect5 = Rect((200, 200), (200, 200))
    rect6 = Rect((400, 200), (200, 200))
    rect7 = Rect((0, 400), (200, 200))
    rect8 = Rect((200, 400), (200, 200))
    rect9 = Rect((400, 400), (200, 200))
    rect = [rect1, rect2, rect3, rect4,
           rect5, rect6, rect7, rect8,
           rect9]
    return rect

def desenhar_tabu(tela):
    pygame.draw.line(tela, (255, 255, 255), (200, 0), (200, 600), 10)
    pygame.draw.line(tela, (255, 255, 255), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (255, 255, 255), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (255, 255, 255), (0, 400), (600, 400), 10)

def testar_posicao(rect, mouse_pos, e, tela):
    for posicao in rect:
        if e.type == MOUSEBUTTONDOWN and posicao.collidepoint(mouse_pos):
            if posicao == rect[0]:
                escolher_jogador((100, 100), tela)

def main():
    """
    """

    pygame.init()
    tela = pygame.display.set_mode((600, 600), 0, 32)
    nome_tela = pygame.display.set_caption('Jogo da velha')
    tabuleiro = criar_tabuleiro()
    rect = definir_rect()



    while True:
        mouse_pos = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == MOUSEBUTTONDOWN:
                testar_posicao(rect, mouse_pos, e, tela)
        desenhar_tabu(tela)
        pygame.display.flip()

vez = 'JOGADOR1'
main()






