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

def test_agregar_con_stock_menor_al_pedido_informa_stock_insuficiente(inventario, carrito, cafe):
    inventario.stock_disponible.return_value = 3
    with pytest.raises(StockInsuficienteError):
        carrito.agregar(cafe, 4)


def test_agregar_producto_existente_suma_las_cantidades(carrito, cafe):
    carrito.agregar(cafe, 2)
    carrito.agregar(cafe, 3)
    assert carrito.cantidad_de(cafe.sku) == 5


def test_agregar_consulta_el_inventario_con_el_sku_del_producto(inventario, carrito, cafe):
    carrito.agregar(cafe, 2)
    inventario.stock_disponible.assert_called_once_with(cafe.sku)


def test_sumar_cantidades_no_puede_superar_el_stock(inventario, carrito, cafe):
    inventario.stock_disponible.return_value = 4
    carrito.agregar(cafe, 3)
    with pytest.raises(StockInsuficienteError):
        carrito.agregar(cafe, 2)