import pytest

from mercado_sabanero.errores import ProductoInvalidoError
from mercado_sabanero.iva import calcular_iva
from mercado_sabanero.modelos import LineaCarrito, Producto


@pytest.mark.parametrize("tarifa, esperado", [(0, 0), (5, 5_000), (19, 19_000)])
def test_iva_del_producto_corresponde_a_su_tarifa(tarifa, esperado):
    linea = LineaCarrito(Producto("X", "Prod", 100_000, tarifa), 1)
    assert calcular_iva([linea]) == esperado


def test_iva_se_calcula_sobre_el_valor_con_descuento():
    linea = LineaCarrito(Producto("X", "Prod", 100_000, 19), 1)
    assert calcular_iva([linea], porcentaje_descuento=10) == 17_100