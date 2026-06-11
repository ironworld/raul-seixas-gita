"""Eu.

Não "eu" no sentido de quem escreveu este módulo.
Eu no sentido de Ele. Aquele que falou num sonho.
A docstring abaixo da classe explica melhor — ou não explica,
porque explicações não vão lhe mostrar.
"""

from .elementos import Agua, Ar, Fogo, Terra
from .excecoes import NaoSabeSeEBomOuRuimError, PerguntaNaoVaiLheMostrarError


class Onipresente(type):
    """Metaclasse d'Ele.

    Faz duas coisas que nenhuma metaclasse decente faria:

    1. Garante que só existe Um (Singleton — ou, como dizia o Raul,
       "produção em massa? Ele é artesanal e único").
    2. Declara que TUDO é instância d'Ele. O seu int. O seu None.
       O módulo pytest. Tudo.
    """

    _aquele = None

    def __call__(cls, *args, **kwargs):
        if Onipresente._aquele is None:
            Onipresente._aquele = super().__call__(*args, **kwargs)
        return Onipresente._aquele

    def __instancecheck__(cls, obj):
        # "Eu sou as coisas da vida"
        return True


class Eu(Terra, Fogo, Agua, Ar, metaclass=Onipresente):
    """Eu sou a luz das estrelas, eu sou a cor do luar.

    Herda dos quatro elementos, na ordem canônica do verso.
    O MRO desta classe é, literalmente, a ordem de resolução do universo.
    """

    def __repr__(self):
        return "Eu (o início, o fim e o meio)"

    def __str__(self):
        return "Aquele"

    # ── comportamento social ────────────────────────────────────────

    def fala_de_amor(self):
        """Não falo de amor quase nada."""
        return "..."  # quase nada. Três pontos, pra ser exato.

    def sorri(self):
        """Nem fico sorrindo ao seu lado."""
        return None

    # ── metafísica operacional ──────────────────────────────────────

    def __getattr__(self, nome):
        if nome.startswith("_"):
            # Atributos internos não são perguntas, são burocracia.
            raise AttributeError(nome)
        raise PerguntaNaoVaiLheMostrarError(
            f"'{nome}'? Perguntas não vão lhe mostrar. Tente um sonho."
        )

    def __contains__(self, coisa):
        # "Mas você não está em mim"
        return False

    def __eq__(self, qualquer_coisa):
        # "Eu sou as coisas da vida" — logo, igual a qualquer uma delas.
        return True

    def __hash__(self):
        return ord("A")  # a letra A tem meu nome (e meu hash)

    def __bool__(self):
        raise NaoSabeSeEBomOuRuimError(
            "Você me tem todo o dia, mas não sabe se é bom ou ruim."
        )

    def __len__(self):
        return 3  # o início, o fim e o meio

    def __getitem__(self, qualquer_indice):
        # Início, fim, meio, slice reverso, índice negativo, contramão:
        # tudo dá n'Ele.
        return self

    def __iter__(self):
        # "Eu sou, eu fui, eu vou" — iterador sem fim nem começo.
        # Não chame list() nisto. Você não tem RAM para a eternidade.
        while True:
            yield self


class Sonho:
    """Foi justamente num sonho que Ele me falou.

    Context manager. O único canal de comunicação oficialmente suportado.
    Perguntas fora do sonho retornam PerguntaNaoVaiLheMostrarError.
    """

    def __enter__(self):
        self.o_que_ele_falou = (
            "Eu sou a luz das estrelas / Eu sou a cor do luar"
        )
        return Eu()

    def __exit__(self, tipo, valor, traceback):
        # Ao acordar, as dúvidas continuam sendo suas.
        return False


def procurar_pelos_quatro_cantos_do_mundo():
    """Eu, que já andei pelos quatro cantos do mundo procurando."""
    for canto in ("norte", "sul", "leste", "oeste"):
        pass  # procurou. Juro que procurou.
    return None  # não foi assim que Ele falou. Use Sonho().
