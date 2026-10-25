import pytest

from mercado_sabanero.puntos import calcular_puntos


@pytest.mark.parametrize("total, esperado", [(999, 0), (1_000, 1), (1_999, 1), (250_515, 250)])
def test_un_punto_por_cada_mil_pesos_completos(total, esperado):
    assert calcular_puntos(total) == esperado
