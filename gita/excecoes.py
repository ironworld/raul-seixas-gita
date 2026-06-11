"""Exceções metafísicas.

Capturá-las é fácil. Compreendê-las, não.
"""


class PerguntaNaoVaiLheMostrarError(AttributeError):
    """Levantada sempre que alguém tenta entender Ele via pergunta.

    Herda de AttributeError por humildade: perguntar a Ele qualquer
    coisa é, tecnicamente, acessar um atributo que você não merece.
    """


class NaoSabeSeEBomOuRuimError(Exception):
    """Você me tem todo o dia. Avaliar, porém, está fora do escopo."""
