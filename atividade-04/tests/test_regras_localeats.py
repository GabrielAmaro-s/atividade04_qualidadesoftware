import pytest

from src.regras_localeats import pedido_atingiu_valor_minimo


RESPONSAVEL = "Gabriel Amaro"

def test_pedido_de_trinta_reais_atinge_o_minimo():
    assert pedido_atingiu_valor_minimo(30) is True


def test_pedido_abaixo_do_minimo_e_rejeitado():
    assert pedido_atingiu_valor_minimo(29.99) is False


def test_pedido_negativo_gera_erro():
    with pytest.raises(ValueError, match="não pode ser negativo"):
        pedido_atingiu_valor_minimo(-1)
