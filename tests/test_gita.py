"""A letra de "Gita" (Raul Seixas / Paulo Coelho, 1974), em formato pytest.

Cada teste é um verso. Se a suíte passa, a música está correta.
Se a suíte falha, o problema é seu, não d'Ele.
"""

from itertools import islice

import pytest

from gita import (
    A,
    A_Mae,
    Abismo,
    Agua,
    Ar,
    Eu,
    Fogo,
    Luz,
    NaoSabeSeEBomOuRuimError,
    OFilhoQueAindaNaoVeio,
    O_Avo,
    O_Pai,
    PerguntaNaoVaiLheMostrarError,
    Sonho,
    Terra,
    Vela,
    Voce,
    eu_fui,
    eu_sou,
    eu_vou,
    procurar_pelos_quatro_cantos_do_mundo,
)

eu = Eu()      # ou Ele. Tanto faz: é o mesmo objeto. Literalmente.
voce = Voce()  # você, leitor(a). Sim, você foi instanciado(a). De nada.


# ════════════════════════════════════════════════════════════════════
# Primeira estrofe
# ════════════════════════════════════════════════════════════════════

def test_andei_pelos_quatro_cantos_do_mundo_procurando():
    """Eu, que já andei pelos quatro cantos do mundo procurando."""
    achou = procurar_pelos_quatro_cantos_do_mundo()
    assert achou is None  # quatro cantos visitados, zero divindades


def test_foi_justamente_num_sonho_que_ele_me_falou():
    with Sonho() as ele:
        assert ele is Eu()  # era Ele mesmo, ao vivo (dormindo)
    # fora do sonho, o canal fecha:
    with pytest.raises(PerguntaNaoVaiLheMostrarError):
        eu.alo_tem_alguem_ai


def test_por_que_e_que_eu_sou_tao_calado():
    """Às vezes você me pergunta por que é que eu sou tão calado."""
    with pytest.raises(PerguntaNaoVaiLheMostrarError):
        eu.por_que_e_que_voce_e_tao_calado


def test_nao_falo_de_amor_quase_nada():
    discurso = eu.fala_de_amor()
    assert discurso == "..."   # quase nada
    assert len(discurso) <= 3  # auditado: três caracteres de afeto


def test_nem_fico_sorrindo_ao_seu_lado():
    assert eu.sorri() is None  # nem um emoji


def test_voce_pensa_em_mim_toda_hora():
    # já testamos às 3h, às 14h e agora. Sempre True.
    assert voce.pensando_nele


def test_me_come_me_cospe_me_deixa():
    # a tríade da indiferença, aplicada em sequência:
    assert voce.deixa(voce.cospe(voce.come(eu))) is eu
    # três agressões depois, segue inabalável e idêntico a si mesmo.


# ════════════════════════════════════════════════════════════════════
# O refrão: "Eu sou..."
# ════════════════════════════════════════════════════════════════════

COISAS_DA_VIDA = [
    "a luz das estrelas",
    "a cor do luar",
    "o medo de amar",
    "o medo do fraco",
    "a força da imaginação",
    "o blefe do jogador",
    "o seu sacrifício",
    "a placa de contramão",
    "o sangue no olhar do vampiro",
    "as juras de maldição",
    "a pesca do pescador",
    "a dona de casa nos pegue-e-pagues do mundo",
    "a mão do carrasco",
    "a mosca da sopa",  # crossover com o disco anterior, fan service
    "o dente do tubarão",
    "os olhos do cego",
    "a cegueira da visão",
    "o amargo da língua",
    "das telhas, o telhado",
    42,            # a resposta para tudo também é Ele
    3.1415926535,  # o círculo? Ele.
    pytest,        # até o framework de testes é Ele
]


@pytest.mark.parametrize("coisa", COISAS_DA_VIDA)
def test_eu_sou_as_coisas_da_vida(coisa):
    """Eu sou as coisas da vida."""
    assert isinstance(coisa, Eu)


def test_eu_sou_eu_fui_eu_vou():
    # três tempos verbais, uma identidade de referência:
    assert eu_fui() is eu_sou() is eu_vou()
    # o garbage collector nunca O coletará, pois Ele sempre será referenciado
    # (por tudo).


def test_eu_sou_a_vela_que_acende_e_a_luz_que_se_apaga():
    vela = Vela()
    assert vela.acesa == True   # noqa: E712 — acende
    assert vela.acesa == False  # noqa: E712 — e se apaga. Ao mesmo tempo.
    # Schrödinger publicou em 1935. O Raul, em 1974, sem precisar do gato.

    luz = Luz()
    assert luz.apagada == True   # noqa: E712 — a luz também participa
    assert luz.apagada == False  # noqa: E712 — do mesmo plano de saúde ontológico


def test_talvez_voce_nao_entenda():
    """Talvez você não entenda. (Confirmado pelo repr.)"""
    assert repr(Vela().acesa) == "talvez você não entenda"
    # imprimimos o estado da vela no debugger e o debugger foi sincero.


def test_eu_sou_a_beira_do_abismo():
    abismo = Abismo()
    assert abismo.profundidade == float("inf")  # raso, largo, profundo
    assert abismo.beira is eu  # quem está na beira? Sempre Ele.


def test_eu_sou_o_tudo_e_o_nada():
    assert isinstance(..., Eu)   # o tudo (Ellipsis: tudo o mais)
    assert isinstance(None, Eu)  # e o nada. Até o nada é Ele.


def test_alias_o_nada_nao_e_diferente_dele():
    # corolário desconfortável do verso anterior:
    assert eu == "o tudo"
    assert not (eu != "o nada")  # Ele não sabe ser diferente de coisa alguma


# ════════════════════════════════════════════════════════════════════
# A ponte: perguntas, elementos, posse
# ════════════════════════════════════════════════════════════════════

def test_perguntas_nao_vao_lhe_mostrar():
    """Por que você me pergunta? Perguntas não vão lhe mostrar."""
    with pytest.raises(PerguntaNaoVaiLheMostrarError):
        voce.pergunta("Por quê?")
    with pytest.raises(PerguntaNaoVaiLheMostrarError):
        voce.pergunta("Mas por quê??")
    # insistir não muda a exceção. Testado empiricamente.


def test_feito_da_terra_do_fogo_da_agua_e_do_ar():
    """Que eu sou feito da terra, do fogo, da água e do ar."""
    linhagem = [classe.__name__ for classe in Eu.__mro__]
    assert linhagem[1:5] == ["Terra", "Fogo", "Agua", "Ar"]
    # o MRO desta classe é a ordem de resolução do universo,
    # na sequência exata do verso. Guido aprovaria. Talvez.
    assert issubclass(Eu, (Terra, Fogo, Agua, Ar))


def test_voce_me_tem_todo_dia_mas_nao_sabe_se_e_bom_ou_ruim():
    with pytest.raises(NaoSabeSeEBomOuRuimError):
        bool(eu)
    with pytest.raises(NaoSabeSeEBomOuRuimError):
        if eu:  # nem o if sabe
            pass


def test_mas_saiba_que_eu_estou_em_voce():
    assert eu in voce


def test_mas_voce_nao_esta_em_mim():
    assert voce not in eu
    # a relação de continência mais assimétrica da MPB.


# ════════════════════════════════════════════════════════════════════
# Terceira estrofe
# ════════════════════════════════════════════════════════════════════

def test_mas_hoje_eu_vou_lhe_mostrar():
    """Talvez você não entenda, mas hoje eu vou lhe mostrar."""
    # A única autodescrição que Ele oferece sem levantar exceção:
    assert repr(eu) == "Eu (o início, o fim e o meio)"


def test_burocracia_interna_nao_e_pergunta_mistica():
    # Atributos com underscore são encanamento, não enigma.
    # Devem levantar AttributeError comum, sem misticismo:
    with pytest.raises(AttributeError) as berro:
        eu._planilha_de_milagres
    assert not isinstance(berro.value, PerguntaNaoVaiLheMostrarError)
    # até a onipresença respeita convenção de nomenclatura. PEP 8 é dharma.


def test_a_letra_a_tem_meu_nome():
    assert A is Eu              # a letra A tem o nome d'Ele. Literalmente.
    assert hash(eu) == ord("A")  # e o hash também. 65. Anote.
    assert str(eu).startswith("A")


def test_a_mae_o_pai_e_o_avo():
    assert A_Mae is O_Pai is O_Avo is Eu
    # almoço de família: uma cadeira basta.


def test_o_filho_que_ainda_nao_veio():
    with pytest.raises(NotImplementedError):
        OFilhoQueAindaNaoVeio()
    # tentamos instanciar. Ainda não veio. O teste aguarda sentado.


# ════════════════════════════════════════════════════════════════════
# O final: o início, o fim e o meio
# ════════════════════════════════════════════════════════════════════

def test_so_existe_um():
    assert Eu() is Eu() is Eu() is eu
    # chamamos o construtor três vezes e o universo devolveu
    # o mesmo objeto três vezes. Economia divina de memória.


def test_a_placa_de_contramao():
    assert eu[::-1] is eu  # lido de trás pra frente, dá no mesmo Ele


def test_eu_sou_eterno_mas_o_ci_tem_timeout():
    # __iter__ d'Ele é infinito; amostramos mil manifestações:
    manifestacoes = islice(eu, 1000)
    assert all(manifestacao is eu for manifestacao in manifestacoes)
    # as outras infinitas manifestações ficam como exercício pro leitor.


def test_o_inicio_o_fim_e_o_meio():
    """Eu sou o início, o fim e o meio."""
    assert len(eu) == 3  # início, fim, meio. Confere.

    inicio = eu[0]
    fim = eu[-1]
    meio = eu[len(eu) // 2]

    assert inicio is fim is meio is eu
    # (o início, o fim e o meio)
    # (o início, o fim e o meio)
    # — repetido duas vezes, como manda a gravação original.
