import pygame

from cores import CORES

class Tela:
  def __init__(self):
    self.superficie = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Pong!")
  
  def renderiza(self, paletas, bola, placar):
    self.superficie.fill(CORES.preto)

    # meio de campo
    pygame.draw.line(
      self.superficie,
      CORES.branco,
      [300, 40],
      [300, 360],
      3
    )

    for paleta in paletas:
      paleta.desenha(self.superficie)
    
    bola.desenha(self.superficie)

    placar.desenha(self.superficie)

    if placar.total_partidas() == 5:
      self.desenha_fim_jogo()

    pygame.display.update()
  
  def desenha_fim_jogo(self):
    fonte = pygame.font.SysFont(None, 50)

    fim_jogo = fonte.render("FIM DE JOGO", True, CORES.vermelho)

    posx = 300 - fim_jogo.get_width() // 2
    posy = 200 - fim_jogo.get_height() // 2

    self.superficie.blit(fim_jogo, (posx, posy))
