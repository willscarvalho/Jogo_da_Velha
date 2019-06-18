
import funcoes as fn

fn.inicio()
tabuleiro = fn.criar_tabuleiro()
jogador1, jogador2 = fn.escolher_jogador()
fn.mostrar_tabuleiro_inicial()
ganhador = ' '
fn.jogo_loop(tabuleiro, jogador1, jogador2, ganhador)
