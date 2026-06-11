"""A mãe, o pai e o avô. E o filho que ainda não veio.

A árvore genealógica mais econômica da música popular brasileira:
todos os ancestrais são o mesmo objeto.
"""

from .eu import Eu

A_Mae = Eu   # a mãe
O_Pai = Eu   # o pai
O_Avo = Eu   # e o avô — almoço de domingo bem barato


class OFilhoQueAindaNaoVeio:
    """O filho que ainda não veio."""

    def __new__(cls, *args, **kwargs):
        raise NotImplementedError(
            "O filho ainda não veio. Tente novamente na próxima encarnação."
        )
