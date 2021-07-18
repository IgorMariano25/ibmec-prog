import math
import random

import pygame

class Bola:
  velocidade = 5
  posicao = [290, 190]

  def __init__(self):
    self.direcao = self.cria_vetor_unitario()

    pygame.mixer.init()
    self.som = pygame.mixer.Sound("assets\\bola.wav")

  def desenha(self, tela):
    imagem = pygame.image.load("assets\\bola.png")
    # imagem = pygame.transform.scale(imagem, (20, 20))

    tela.blit(imagem, self.posicao)
  
  def cria_vetor_unitario(self):
    while True:
      dir_x = random.uniform(-1, 1)
      if int(dir_x * self.velocidade):
        break

    dir_y = random.choice([-1, 1]) * math.sqrt(1 - dir_x ** 2)
    return [dir_x, dir_y]
  
  def movimenta(self):
    self.posicao = [
      int(self.posicao[0] + self.velocidade * self.direcao[0]),
      int(self.posicao[1] + self.velocidade * self.direcao[1])
    ]

    self.verifica_colisoes()
  
  def verifica_colisoes(self):
    if self.posicao[1] < 0:
      self.direcao[1] *= -1
      self.posicao[1] = 0
    
    if self.posicao[1] > 380:
      self.direcao[1] *= -1
      self.posicao[1] = 380
    
    if self.posicao[0] < 40:
      self.direcao[0] *= -1
      self.posicao[0] = 40
    
    if self.posicao[0] > 540:
      self.direcao[0] *= -1
      self.posicao[0] = 540

  def acelera(self):
    self.velocidade += 1
