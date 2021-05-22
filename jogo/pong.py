"""Código principal do jogo."""
import math
import random

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


class Paleta:
    """Paleta para refletir a bola."""
    velocidade: int = 5

    def __init__(self, posicao: List[int], dimensoes: List[int], acoes: List[int], limites: List[int]) -> None:
        self.largura = dimensoes[0]
        self.altura = dimensoes[1]
        self.posicao = posicao
        self.subir = acoes[0]
        self.descer = acoes[1]
        self.limite_inferior = limites[0]
        self.limite_superior = limites[1]

    def desenha(self, tela: pygame.Surface) -> None:
        """Desenha uma paleta na tela."""
        pygame.draw.rect(
            tela,
            Cores.branco,
            self.posicao + [self.largura, self.altura]
        )

    def esta_movimentando(self, teclas: List[bool]) -> bool:
        """Retorna True caso uma das teclas de movimento esteja pressionada."""
        return any((teclas[self.subir], teclas[self.descer]))

    def movimenta(self, teclas: List[bool]) -> None:
        """Movimenta a paleta conforme as teclas que estão pressionadas."""
        if teclas[self.subir] and self.posicao[1] > self.limite_superior:
            self.posicao[1] -= self.velocidade

        if teclas[self.descer] and self.posicao[1] + self.altura < self.limite_inferior:
            self.posicao[1] += self.velocidade


class Bola:
    """Bola que irá se movimentar pela tela."""
    velocidade: int = 10

    def __init__(self, posicao: List[int], raio: int) -> None:
        self.posicao = posicao
        self.raio = raio
        self.direcao = cria_vetor_unitario()

    def desenha(self, tela: pygame.Surface) -> None:
        """Desenha a bola na tela."""
        pygame.draw.circle(
            tela,
            Cores.branco,
            self.posicao,
            self.raio
        )

    def movimenta(self) -> None:
        """Movimenta a bola."""
        self.posicao = [
            int(self.posicao[0] + self.velocidade * self.direcao[0]),
            int(self.posicao[1] + self.velocidade * self.direcao[1]),
        ]


class Tela:
    """Informações sobre a tela."""
    def __init__(self, largura: int, altura: int) -> None:
        self.largura: int = largura
        self.altura: int = altura
        self.tela: pygame.Surface = self.cria_tela()

        self.limites: List[int] = [
            altura - Bordas.margem - Bordas.espessura // 2,
            Bordas.margem + Bordas.espessura // 2
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

    def cria_tela(self) -> pygame.Surface:
        """Cria a tela básica do jogo."""
        tela: pygame.Surface = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Pong!")

        return tela

    def renderiza(self) -> None:
        """Preenche o fundo da tela."""
        self.tela.fill(Cores.preto)

        for paleta in self.paletas:
            paleta.desenha(self.tela)

        self.bola.desenha(self.tela)

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
        posicao_inicial = (self.largura // 2, self.altura // 2)

        return Bola(posicao_inicial, 10)


def cria_vetor_unitario() -> List[float]:
    """Cria um vetor unitário [x, y] com a direção da bola."""
    while True:
        dir_x = random.uniform(-1.0, 1.0)
        if dir_x:
            break

    return [dir_x, random.choice([-1, 1]) * math.sqrt(1 - dir_x ** 2)]


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
