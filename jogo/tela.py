"""Tela do jogo, com todas as interações e ações."""
import time

from typing import List, Tuple

import pygame

from .constantes import BORDAS, CORES
from .paleta import Paleta
from .bola import Bola


class Tela:
    """Informações sobre a tela."""
    def __init__(self, largura: int, altura: int) -> None:
        self.largura: int = largura
        self.altura: int = altura
        self.pontos: List[int] = [0, 0]
        self.tela: pygame.Surface = self.cria_tela()

        self.limites: List[int] = [
            altura - BORDAS.margem - BORDAS.espessura // 2,
            BORDAS.margem + BORDAS.espessura // 2
        ]
        self.paletas: List[Paleta] = self.cria_paletas()

        # Ferindo encapsulamento aqui. Melhorar em algum momento...
        self.limites.extend(
            [
                self.paletas[0].posicao[0] + self.paletas[0].largura,
                self.paletas[1].posicao[0]
            ]
        )
        self.bola: Bola = self.cria_bola()

    def inicia_partida(self) -> None:
        """Reposiciona paletas e bola para uma nova partida."""
        time.sleep(0.5)
        self.paletas: List[Paleta] = self.cria_paletas()
        self.bola: Bola = self.cria_bola()

    def cria_tela(self) -> pygame.Surface:
        """Cria a tela básica do jogo."""
        tela: pygame.Surface = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Pong!")

        return tela

    def renderiza(self) -> None:
        """Preenche o fundo da tela."""
        self.tela.fill(CORES.preto)

        for paleta in self.paletas:
            paleta.desenha(self.tela)

        self.bola.desenha(self.tela)

        self.desenha_meio_campo()
        self.desenha_bordas()
        self.desenha_pontuacao()
        pygame.display.update()

    def desenha_pontuacao(self) -> None:
        """Desenha pontuação na tela."""
        font: pygame.font.Font = pygame.font.SysFont(None, 50)

        p1_pontos = font.render(str(self.pontos[0]), True, CORES.vermelho)
        p2_pontos = font.render(str(self.pontos[1]), True, CORES.vermelho)

        self.tela.blit(p1_pontos, (15, 20))
        self.tela.blit(p2_pontos, (self.largura - 35, 20))

    def desenha_meio_campo(self) -> None:
        """Desenha o meio de campo do jogo."""
        pygame.draw.line(
            self.tela,
            CORES.branco,
            [self.largura // 2, self.altura // 10],
            [self.largura // 2, 9 * self.altura // 10],
            BORDAS.espessura
        )

    def desenha_bordas(self) -> None:
        """Desenha as bordas do campo na tela."""
        retangulo: List[int] = [
            BORDAS.margem,
            BORDAS.margem,
            self.largura - BORDAS.margem * 2,
            self.altura - BORDAS.margem * 2
        ]

        pygame.draw.rect(
            self.tela,
            CORES.branco,
            retangulo,
            BORDAS.espessura
        )

    def cria_paletas(self) -> List[Paleta]:
        """Inicializa as paletas da tela."""
        dimensoes: List[int] = [20, 200]

        posicoes_iniciais: Tuple[List[int]] = (
            [self.largura // 20, (self.altura - dimensoes[1]) // 2],
            [19 * self.largura // 20 - dimensoes[0], (self.altura - dimensoes[1]) // 2]
        )

        return [
            Paleta(posicoes_iniciais[0], dimensoes, [pygame.K_w, pygame.K_s], self.limites[:2]),
            Paleta(posicoes_iniciais[1], dimensoes, [pygame.K_UP, pygame.K_DOWN], self.limites[:2])
        ]

    def cria_bola(self) -> Bola:
        """Inicializa a bola da tela."""
        posicao_inicial: List[int] = [self.largura // 2, self.altura // 2]

        return Bola(posicao_inicial, 10, self.limites)

    def atualiza_jogo(self) -> None:
        """Analisa a situação do jogo e age caso um ponto seja feito."""
        if self.bola.posicao[0] - self.bola.raio == self.limites[2] and \
                (self.bola.posicao[1] < self.paletas[0].posicao[1] or \
                 self.bola.posicao[1] > self.paletas[0].posicao[1] + self.paletas[0].altura):
            self.pontos[1] += 1
            self.inicia_partida()

        if self.bola.posicao[0] + self.bola.raio == self.limites[3] and \
                (self.bola.posicao[1] < self.paletas[1].posicao[1] or \
                 self.bola.posicao[1] > self.paletas[1].posicao[1] + self.paletas[1].altura):
            self.pontos[0] += 1
            self.inicia_partida()
