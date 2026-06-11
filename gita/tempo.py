"""Eu sou, eu fui, eu vou.

Três funções, três tempos verbais, um único objeto.
O tempo é uma ilusão; a identidade de referência, não.
"""

from .eu import Eu


def eu_fui():
    """Pretérito perfeito. Perfeito mesmo: idêntico ao presente."""
    return Eu()


def eu_sou():
    """Presente do indicativo. Indica sempre a mesma coisa."""
    return Eu()


def eu_vou():
    """Futuro. Spoiler: é o mesmo objeto."""
    return Eu()
