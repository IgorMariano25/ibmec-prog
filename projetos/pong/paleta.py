import pygame

from cores import CORES

class Paleta:
  velocidade = 5
  altura = 150

  def __init__(self, posicao, acoes):
    self.posicao = posicao # [posx, posy]
    self.botao_subir = acoes[0]
    self.botao_descer = acoes[1]
  
  def desenha(self, tela):
    pygame.draw.rect(tela, CORES.branco, self.posicao + [10, self.altura])
  
  def movimenta(self, teclas):
    """
    Realiza o movimento da paleta com base na velocidade da mesma.
    A paleta só é movimentada se algum botão de ação tiver sido acionado em `teclas`.

    Parâmetros:
    teclas -> Lista com booleanos representando o estado de pressionamento de cada tecla.
    """
    if teclas[self.botao_descer] and self.posicao[1] < 400 - self.altura:
      self.posicao[1] += self.velocidade
    
    if teclas[self.botao_subir] and self.posicao[1] > 0:
      self.posicao[1] -= self.velocidade

  def encolhe(self):
    self.altura -= 5
