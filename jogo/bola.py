"""Bola do jogo."""
import math
import random

from typing import List

import pygame

from .constantes import CORES


class Bola:
    """Bola que irá se movimentar pela tela."""
    velocidade: int = 5

    def __init__(self, posicao: List[int], raio: int, limites: List[int]) -> None:
        self.posicao: List[int] = posicao
        self.raio: int = raio
        self.direcao: List[float] = self.cria_vetor_unitario()
        self.limites: List[int] = limites

    def desenha(self, tela: pygame.Surface) -> None:
        """Desenha a bola na tela."""
        pygame.draw.circle(
            tela,
            CORES.branco,
            self.posicao,
            self.raio
        )

    def cria_vetor_unitario(self) -> List[float]:
        """Cria um vetor unitário [x, y] com a direção da bola."""
        while True:
            dir_x: float = random.uniform(-1.0, 1.0)
            if int(dir_x * self.velocidade):
                break

        return [dir_x, random.choice([-1, 1]) * math.sqrt(1 - dir_x ** 2)]

    def movimenta(self) -> None:
        """Movimenta a bola."""
        self.posicao: List[int] = [
            int(self.posicao[0] + self.velocidade * self.direcao[0]),
            int(self.posicao[1] + self.velocidade * self.direcao[1]),
        ]

        self.ajusta_posicao_nos_limites()

    def ajusta_posicao_nos_limites(self) -> None:
        """Corrige a posição da bola caso ela tenha passado dos limites."""
        if self.posicao[1] + self.raio > self.limites[0]:
            self.direcao[1] *= -1
            self.posicao[1] = self.limites[0] - self.raio

        if self.posicao[1] - self.raio < self.limites[1]:
            self.direcao[1] *= -1
            self.posicao[1] = self.limites[1] + self.raio

        if self.posicao[0] - self.raio < self.limites[2]:
            self.direcao[0] *= -1
            self.posicao[0] = self.limites[2] + self.raio
            self.aumenta_velocidade()

        if self.posicao[0] + self.raio > self.limites[3]:
            self.direcao[0] *= -1
            self.posicao[0] = self.limites[3] - self.raio
            self.aumenta_velocidade()

    def aumenta_velocidade(self) -> None:
        """Incrementa a velocidade da bola."""
        self.velocidade += 1
