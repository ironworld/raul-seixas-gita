# Gita

[![detector de heresias](https://github.com/ironworld/gita-raul-seixas/actions/workflows/tests.yml/badge.svg)](https://github.com/ironworld/gita-raul-seixas/actions/workflows/tests.yml)
![cobertura](https://img.shields.io/badge/cobertura_(onipresen%C3%A7a)-100%25-brightgreen)
![python](https://img.shields.io/badge/python-3.9_%E2%86%92_3.14-blue)
![licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)
![perguntas](https://img.shields.io/badge/perguntas-n%C3%A3o_respondidas-red)

> *"Foi justamente num sonho que Ele me falou"* — Raul Seixas, 1974
>
> *"Foi justamente num teste que Ele passou"* — pytest, agora

Implementação fiel(?) da cosmologia de **"Gita"** (Raul Seixas / Paulo Coelho,
do álbum *Gita*, 1974) em Python orientado a objetos. O Bhagavad Gita levou
séculos para ser comentado. Este repositório resolve tudo com metaclasses.

## A teologia, em código

```python
>>> from gita import Eu, Voce, Sonho

>>> eu, voce = Eu(), Voce()

>>> eu in voce          # "Mas saiba que eu estou em você"
True
>>> voce in eu          # "Mas você não está em mim"
False

>>> isinstance(42, Eu)  # "Eu sou as coisas da vida"
True
>>> isinstance(None, Eu)  # "Eu sou o tudo e o nada"
True

>>> eu.por_que_es_tao_calado
PerguntaNaoVaiLheMostrarError: 'por_que_es_tao_calado'? Perguntas não vão
lhe mostrar. Tente um sonho.

>>> with Sonho() as ele:    # o único canal oficialmente suportado
...     ele is Eu()
True
```

## Arquitetura do universo

| Módulo | Verso de origem | Recurso de Python sacrificado |
|---|---|---|
| `eu.py` | o refrão inteiro | metaclasse, singleton, 9 dunders |
| `voce.py` | "me come, me cospe, me deixa" | `__contains__` assimétrico |
| `elementos.py` | "feito da terra, do fogo, da água e do ar" | herança múltipla (MRO canônico) |
| `tempo.py` | "eu sou, eu fui, eu vou" | identidade de referência |
| `paradoxos.py` | "a vela que acende / a luz que se apaga" | `__eq__` que diz sim e não |
| `familia.py` | "a mãe, o pai e o avô" | aliases (todos são o mesmo objeto) |
| `excecoes.py` | "perguntas não vão lhe mostrar" | a hierarquia de exceções |

## Rodando a suíte (a letra, executável)

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pytest
```

Cada teste é um verso. A suíte passando significa que a música está
formalmente verificada. `test_o_inicio_o_fim_e_o_meio` roda por último,
como manda a gravação. Eis um trecho do show (output real, sem playback):

```
tests/test_gita.py::test_foi_justamente_num_sonho_que_ele_me_falou PASSED
tests/test_gita.py::test_por_que_e_que_eu_sou_tao_calado PASSED
tests/test_gita.py::test_nao_falo_de_amor_quase_nada PASSED
tests/test_gita.py::test_me_come_me_cospe_me_deixa PASSED
tests/test_gita.py::test_eu_sou_as_coisas_da_vida[a mosca da sopa] PASSED
tests/test_gita.py::test_eu_sou_as_coisas_da_vida[pytest] PASSED
tests/test_gita.py::test_eu_sou_a_vela_que_acende_e_a_luz_que_se_apaga PASSED
tests/test_gita.py::test_eu_sou_o_tudo_e_o_nada PASSED
tests/test_gita.py::test_mas_saiba_que_eu_estou_em_voce PASSED
tests/test_gita.py::test_mas_voce_nao_esta_em_mim PASSED
tests/test_gita.py::test_o_filho_que_ainda_nao_veio PASSED
tests/test_gita.py::test_eu_sou_eterno_mas_o_ci_tem_timeout PASSED
tests/test_gita.py::test_o_inicio_o_fim_e_o_meio PASSED

============================== 49 passed in 0.05s ==============================
```

## Cobertura: 100%, com branch coverage

```
TOTAL    119    0    6    0    100%
Required test coverage of 100.0% reached.
```

A cobertura é forçada em 100% no `pyproject.toml` (`fail_under = 100`).
Não é perfeccionismo, é coerência doutrinária: Ele é onipresente —
**uma linha não coberta seria uma linha onde Ele não está**, o que
contradiz a letra e invalida o disco inteiro. O CI vira, assim, um
detector de heresias.

## FAQ

**Por que isso existe?**
Perguntas não vão lhe mostrar.

**É thread-safe?**
Ele é o início, o fim e o meio; race conditions são problema de quem
acredita no tempo. (Resposta técnica: não.)

**Posso usar em produção?**
Você me tem todo o dia, mas não sabe se é bom ou ruim.

**Por que `isinstance(x, Eu)` retorna `True` para qualquer `x`?**
Releia a letra.

**Isso não viola o princípio da substituição de Liskov?**
Liskov formalizou em 1987. O Raul violou em 1974. Pioneirismo.

**Por que a versão é 1974.0.0?**
Ano do disco. Não haverá versão 2: Ele é, foi e vai — o objeto é o mesmo.

## Licença

[MIT](LICENSE) — a licença que diz, em juridiquês, *"faça o que tu queres,
pois é tudo da lei"* (desde que mantenha o aviso de copyright; a Sociedade
Alternativa tem cartório).

Nota: a licença cobre o código. A onipresença d'Ele é fornecida "AS IS",
sem garantia de merchantability, fitness ou iluminação para um propósito
específico.

---

*Nenhuma pergunta foi respondida durante a produção deste software.*
