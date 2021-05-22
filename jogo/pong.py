"""Código principal do jogo."""
from dataclasses import dataclass
from typing import Tuple, List

import pygame


@dataclass
class Bordas:
    """Informações sobre as bordas da tela."""
    margem: int = 10
    espessura: int = 3


@dataclass
class Cores:
    """Cores para a tela e objetos."""
    preto: Tuple[int] = (0, 0, 0)
    branco: Tuple[int] = (255, 255, 255)


class Tela:
    """Informações sobre a tela."""
    def __init__(self, largura: int, altura: int) -> None:
        self.largura = largura
        self.altura = altura
        self.tela: pygame.Surface = self.cria_tela()

    def cria_tela(self) -> pygame.Surface:
        """Cria a tela básica do jogo."""
        tela: pygame.Surface = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Pong!")

        return tela

    def renderiza(self) -> None:
        """Preenche o fundo da tela."""
        self.tela.fill(Cores.preto)

        self.desenha_meio_campo()
        self.desenha_bordas()
        pygame.display.update()

    def desenha_meio_campo(self) -> None:
        """Desenha o meio de campo do jogo."""
        pygame.draw.line(
            self.tela,
            Cores.branco,
            [self.largura // 2, self.altura // 10],
            [self.largura // 2, 9 * self.altura // 10],
            Bordas.espessura
        )

    def desenha_bordas(self) -> None:
        """Desenha as bordas do campo na tela."""
        retangulo: List[int] = [
            Bordas.margem,
            Bordas.margem,
            self.largura - Bordas.margem * 2,
            self.altura - Bordas.margem * 2
        ]

        pygame.draw.rect(
            self.tela,
            Cores.branco,
            retangulo,
            Bordas.espessura
        )






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
