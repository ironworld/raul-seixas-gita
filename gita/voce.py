"""Você.

Sim, você. Que pensa n'Ele toda hora. Que come, cospe e deixa.
Este módulo não julga. Ele também não (na verdade Ele não consegue:
veja Eu.__bool__).
"""

from .eu import Eu
from .excecoes import PerguntaNaoVaiLheMostrarError


class Voce:
    """Você me tem todo o dia (mas não sabe se é bom ou ruim)."""

    # "Você pensa em mim toda hora" — toda hora que checarem, está True.
    pensando_nele = True

    def __contains__(self, alguem):
        # "Mas saiba que eu estou em você"
        # (e como tudo é Ele, tem bastante gente aí dentro)
        return isinstance(alguem, Eu)

    def pergunta(self, qualquer_pergunta):
        """Por que você me pergunta? Perguntas não vão lhe mostrar."""
        raise PerguntaNaoVaiLheMostrarError(
            f"{qualquer_pergunta!r}? Boa pergunta. É exatamente esse o problema."
        )

    # "Me come, me cospe, me deixa" — a tríade da indiferença.
    # Note que nenhum dos três métodos consegue alterá-Lo.

    def come(self, ele):
        return ele  # engolido inteiro, devolvido intacto

    def cospe(self, ele):
        return ele  # nem a saliva gruda n'Ele

    def deixa(self, ele):
        return ele  # deixar pra lá também não funciona
