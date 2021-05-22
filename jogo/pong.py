"""Código principal do jogo."""
from dataclasses import dataclass

import pygame


@dataclass
class Tela:
    """Informações sobre a tela."""
    largura: int = 800
    altura: int = 600


def inicio_jogo() -> pygame.Surface:
    """Inicializa o jogo."""
    pygame.init()
    tela = pygame.display.set_mode((Tela.largura, Tela.altura))
    pygame.display.set_caption("Pong!")

    return tela


def jogo() -> None:
    """Entrada do jogo."""
    tela: pygame.Surface = inicio_jogo()
