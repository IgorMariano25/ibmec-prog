"""Código principal do jogo."""
from dataclasses import dataclass
from typing import Tuple

import pygame


@dataclass
class Tela:
    """Informações sobre a tela."""
    largura: int = 800
    altura: int = 600
    tela = None

    def __init__(self) -> None:
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Pong!")

    def renderiza(self) -> None:
        """Preenche o fundo da tela."""
        self.tela.fill(Cores.branco)
        pygame.display.update()


@dataclass
class Cores:
    """Cores para a tela e objetos."""
    branco: Tuple[int] = (255, 255, 255)


def inicio_jogo() -> Tela:
    """Inicializa o jogo."""
    pygame.init()
    return Tela()


def define_taxa_quadros(fps: int):
    """Define a velocidade de execução do jogo em quadros por segundo."""
    pygame.time.Clock().tick(fps)


def trata_eventos() -> bool:
    """Trata os eventos ocorridos entre cada quadro."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

    return False


def roda_loop(tela: Tela) -> None:
    """Roda o loop principal do jogo."""
    while True:
        if trata_eventos():
            break
        tela.renderiza()
        define_taxa_quadros(60)


def encerra_jogo() -> None:
    """Encerra o jogo."""
    print("Saindo do jogo!")
    pygame.quit()


def jogo() -> None:
    """Entrada do jogo."""
    tela: Tela = inicio_jogo()
    roda_loop(tela)
    encerra_jogo()
