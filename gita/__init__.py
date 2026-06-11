"""gita — a cosmologia de Raul Seixas e Paulo Coelho (1974), agora com dunders.

>>> from gita import Eu, Voce
>>> eu, voce = Eu(), Voce()
>>> eu in voce
True
>>> voce in eu
False

Qualquer dúvida, consulte um Sonho(). Perguntas não vão lhe mostrar.
"""

from .elementos import Agua, Ar, Fogo, Terra
from .eu import Eu, Onipresente, Sonho, procurar_pelos_quatro_cantos_do_mundo
from .excecoes import NaoSabeSeEBomOuRuimError, PerguntaNaoVaiLheMostrarError
from .familia import A_Mae, OFilhoQueAindaNaoVeio, O_Avo, O_Pai
from .paradoxos import Abismo, Luz, SimENao, Vela
from .tempo import eu_fui, eu_sou, eu_vou

# "A letra A tem meu nome" — literalmente.
A = Eu

__all__ = [
    "A",
    "A_Mae",
    "Abismo",
    "Agua",
    "Ar",
    "Eu",
    "Fogo",
    "Luz",
    "NaoSabeSeEBomOuRuimError",
    "OFilhoQueAindaNaoVeio",
    "O_Avo",
    "O_Pai",
    "Onipresente",
    "PerguntaNaoVaiLheMostrarError",
    "SimENao",
    "Sonho",
    "Terra",
    "Vela",
    "Voce",
    "eu_fui",
    "eu_sou",
    "eu_vou",
    "procurar_pelos_quatro_cantos_do_mundo",
]

from .voce import Voce  # noqa: E402  (Você vem depois d'Ele. Sempre.)

__version__ = "1974.0.0"  # ano do disco. Semver é para quem acredita no tempo.
