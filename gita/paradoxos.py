"""Paradoxos.

"Eu sou a vela que acende / Eu sou a luz que se apaga"

A física quântica resolveu isso com superposição.
O Raul resolveu onze anos antes, com violão.
"""

from .eu import Eu


class SimENao:
    """Valor de verdade raulseixista.

    É igual a True. É igual a False. Talvez você não entenda,
    mas hoje ele vai lhe mostrar.
    """

    def __eq__(self, valor):
        return isinstance(valor, bool)

    def __repr__(self):
        return "talvez você não entenda"


class Vela:
    """Eu sou a vela que acende."""

    @property
    def acesa(self):
        return SimENao()


class Luz:
    """Eu sou a luz que se apaga."""

    @property
    def apagada(self):
        return SimENao()


class Abismo:
    """Eu sou a beira do abismo."""

    profundidade = float("inf")  # sou raso, largo, profundo

    @property
    def beira(self):
        # Quem está na beira do abismo? Ele. Sempre Ele.
        # (Se você olhar muito tempo para esta property,
        # esta property olha de volta. — Nietzsche, beta tester)
        return Eu()
