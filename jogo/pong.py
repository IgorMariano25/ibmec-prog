"""Código principal do jogo."""
from typing import List

import pygame

from .paleta import Paleta
from .tela import Tela


def inicio_jogo() -> Tela:
    """Inicializa o jogo."""
    pygame.init()
    return Tela(800, 600)


def define_taxa_quadros(fps: int):
    """Define a velocidade de execução do jogo em quadros por segundo."""
    pygame.time.Clock().tick(fps)


def trata_eventos() -> bool:
    """Trata os eventos ocorridos entre cada quadro."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

    return False


def trata_teclas_pressionadas(paletas: List[Paleta]) -> None:
    """Trata o pressionamento de teclas que movimentam as paletas."""
    teclas: List[bool] = pygame.key.get_pressed()
    if any((paleta.esta_movimentando(teclas) for paleta in paletas)):
        for paleta in paletas:
            paleta.movimenta(teclas)


def roda_loop(tela: Tela) -> None:
    """Roda o loop principal do jogo."""
    while True:
        trata_teclas_pressionadas(tela.paletas)
        if trata_eventos():
            break
        tela.bola.movimenta()
        tela.atualiza_jogo()
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
