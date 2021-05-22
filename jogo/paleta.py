"""Paletas do jogo."""
from typing import List

import pygame

from .constantes import CORES


class Paleta:
    """Paleta para refletir a bola."""
    velocidade: int = 5

    def __init__(self, posicao: List[int], dimensoes: List[int], acoes: List[int], limites: List[int]) -> None:
        self.largura: int = dimensoes[0]
        self.altura: int = dimensoes[1]
        self.posicao: List[int] = posicao
        self.subir: int = acoes[0]
        self.descer: int = acoes[1]
        self.limites: List[int] = limites

    def desenha(self, tela: pygame.Surface) -> None:
        """Desenha uma paleta na tela."""
        pygame.draw.rect(
            tela,
            CORES.branco,
            self.posicao + [self.largura, self.altura]
        )

    def esta_movimentando(self, teclas: List[bool]) -> bool:
        """Retorna True caso uma das teclas de movimento esteja pressionada."""
        return any((teclas[self.subir], teclas[self.descer]))

    def movimenta(self, teclas: List[bool]) -> None:
        """Movimenta a paleta conforme as teclas que estão pressionadas."""
        if teclas[self.subir] and self.posicao[1] > self.limites[1]:
            self.posicao[1] -= self.velocidade

        if teclas[self.descer] and self.posicao[1] + self.altura < self.limites[0]:
            self.posicao[1] += self.velocidade
