import time

import pygame

from tela import Tela
from bola import Bola
from placar import Placar
from paleta import Paleta

class Gerenciadora:
  def __init__(self):
    self.tela = Tela()
    self.placar = Placar()
    self.inicia_partida()

  def inicia_partida(self):
    time.sleep(0.5)
    self.paletas = [
      Paleta([30, 125], [pygame.K_w, pygame.K_s]),
      Paleta([560, 125], [pygame.K_UP, pygame.K_DOWN])
    ]
    self.bola = Bola()

  def roda_loop(self):
    while True:
      cliques = self.monitora_cliques()

      if pygame.QUIT in cliques:
        break

      if self.placar.total_partidas() < 5:
        self.movimenta_objetos()

        if self.placar.atualiza(self.paletas, self.bola):
          self.inicia_partida()
        
        self.tela.renderiza(self.paletas, self.bola, self.placar)
      else:
        if pygame.MOUSEBUTTONUP in cliques:
          # Verificar coordenadas do mouse:
          # pygame.mouse.get_pos()
          self.placar = Placar()

      pygame.time.Clock().tick(60)

  def monitora_cliques(self):
    cliques = []

    for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
        cliques.append(pygame.QUIT)
      
      if evento.type == pygame.MOUSEBUTTONUP:
        cliques.append(pygame.MOUSEBUTTONUP)

    return cliques

  def movimenta_objetos(self):
    teclas = pygame.key.get_pressed()
    for paleta in self.paletas:
      paleta.movimenta(teclas)
    
    self.bola.movimenta()
