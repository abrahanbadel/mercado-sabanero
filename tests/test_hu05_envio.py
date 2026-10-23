import pytest

from mercado_sabanero.envio import calcular_envio
from mercado_sabanero.liquidacion import liquidar
from tests.conftest import carrito_con


@pytest.mark.parametrize(
    "municipio, esperado",
    [("Sincelejo", 8_000), ("sincelejo", 8_000), ("Corozal", 15_000), ("Sampués", 15_000)],
)
def test_envio_segun_municipio(municipio, esperado):
    assert calcular_envio(municipio, 10_000) == esperado

@pytest.mark.parametrize("base, esperado", [(149_999, 8_000), (150_000, 0), (300_000, 0)])
def test_envio_gratis_desde_150000_con_iva(base, esperado):
    assert calcular_envio("Sincelejo", base) == esperado


def test_cupon_enviogratis_deja_el_envio_en_cero():
    assert calcular_envio("Corozal", 10_000, envio_gratis=True) == 0


def test_total_es_subtotal_menos_descuento_mas_iva_mas_envio(inventario, cafe):
    carrito = carrito_con(inventario, cafe, 2)  # 30.000; IVA 1.500; envío 8.000
    res = liquidar(carrito, "Sincelejo")
    assert res.total == res.subtotal - res.descuento + res.iva + res.envio == 39_500



