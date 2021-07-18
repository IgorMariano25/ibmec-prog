import pygame

from gerenciadora import Gerenciadora

def inicia_jogo():
  pygame.init()
  return Gerenciadora()

def encerra_jogo():
  print("Saindo do jogo!")
  pygame.quit()

def jogo():
  gerenciadora = inicia_jogo()
  gerenciadora.roda_loop()
  encerra_jogo()

jogo()
