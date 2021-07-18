# import random

from replit import audio

import pygame

from cores import CORES

class Placar:
  def __init__(self):
    self.p1 = 0
    self.p2 = 0
  
  def atualiza(self, paletas, bola):
    if self.chama_var(paletas[0], bola, 40):
      self.p2 += 1
      return True
    
    if self.chama_var(paletas[1], bola, 540):
      self.p1 += 1
      return True
    
    return False

  def chama_var(self, paleta, bola, limite):
    if bola.posicao[0] == limite:
      if paleta.posicao[1] - 10 < bola.posicao[1] < paleta.posicao[1] + paleta.altura - 10:
        bola.acelera()
        paleta.encolhe()
        bola.som.play()
        # audio.play_file("assets\\bola.wav")
        return False
      
      return True
    
    return False
  
  def desenha(self, superficie):
    fonte = pygame.font.SysFont(None, 30)

    p1_texto = fonte.render(str(self.p1), True, CORES.vermelho)
    p2_texto = fonte.render(str(self.p2), True, CORES.vermelho)

    superficie.blit(p1_texto, (10, 20))
    superficie.blit(p2_texto, (580, 20))
  
  def total_partidas(self):
    return self.p1 + self.p2
