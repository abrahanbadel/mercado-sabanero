import pytest

from mercado_sabanero.descuentos import porcentaje_descuento_volumen


@pytest.mark.parametrize(
    "subtotal, esperado",
    [(0, 0), (199_999, 0), (200_000, 5), (499_999, 5), (500_000, 10), (900_000, 10)],
)
def test_descuento_por_volumen_en_valores_limite(subtotal, esperado):
    assert porcentaje_descuento_volumen(subtotal) == esperado
