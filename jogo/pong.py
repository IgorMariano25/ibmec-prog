"""Código principal do jogo."""
from dataclasses import dataclass
from typing import Tuple

import pygame


@dataclass
class Tela:
    """Informações sobre a tela."""
    largura: int = 800
    altura: int = 600


@dataclass
class Cores:
    """Cores para a tela e objetos."""
    branco: Tuple[int] = (255, 255, 255)


def inicio_jogo() -> pygame.Surface:
    """Inicializa o jogo."""
    pygame.init()
    tela = pygame.display.set_mode((Tela.largura, Tela.altura))
    pygame.display.set_caption("Pong!")

    return tela


def renderiza(tela: pygame.Surface) -> None:
    """Renderiza a tela do jogo."""
    tela.fill(Cores.branco)
    pygame.display.update()


def define_taxa_quadros(fps: int):
    """Define a velocidade de execução do jogo em quadros por segundo."""
    pygame.time.Clock().tick(fps)


def roda_loop(tela: pygame.Surface) -> None:
    """Roda o loop principal do jogo."""
    while True:
        renderiza(tela)
        define_taxa_quadros(60)


def jogo() -> None:
    """Entrada do jogo."""
    tela: pygame.Surface = inicio_jogo()
    roda_loop(tela)
