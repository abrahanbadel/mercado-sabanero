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






