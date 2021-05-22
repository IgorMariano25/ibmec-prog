"""Constantes do projeto."""
from typing import Tuple
from dataclasses import dataclass


@dataclass
class BORDAS:
    """Informações sobre as bordas da tela."""
    margem: int = 10
    espessura: int = 3


@dataclass
class CORES:
    """Cores para a tela e objetos."""
    preto: Tuple[int] = (0, 0, 0)
    branco: Tuple[int] = (255, 255, 255)
    vermelho: Tuple[int] = (255, 0, 0)
