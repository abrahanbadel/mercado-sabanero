import pytest

from mercado_sabanero.errores import CantidadInvalidaError, StockInsuficienteError


@pytest.mark.parametrize("cantidad", [1, 25, 50])
def test_agregar_cantidad_valida_deja_el_producto_en_el_carrito(carrito, cafe, cantidad):
    # Arrange: inventario (mock) con stock suficiente (fixture)
    # Act
    carrito.agregar(cafe, cantidad)
    # Assert
    assert carrito.cantidad_de(cafe.sku) == cantidad

@pytest.mark.parametrize("cantidad", [0, 51, -1])
def test_agregar_cantidad_fuera_de_rango_lanza_error(carrito, cafe, cantidad):
    with pytest.raises(CantidadInvalidaError):
        carrito.agregar(cafe, cantidad)
    assert carrito.esta_vacio()

