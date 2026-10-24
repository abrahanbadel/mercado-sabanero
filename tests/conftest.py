from unittest.mock import Mock

import pytest

from mercado_sabanero.carrito import Carrito
from mercado_sabanero.modelos import Producto


@pytest.fixture
def inventario():
    mock = Mock()
    mock.stock_disponible.return_value = 1_000
    return mock


@pytest.fixture
def carrito(inventario):
    return Carrito(inventario)


@pytest.fixture
def cafe():
    return Producto("CAF-1", "Café", 15_000, 5)


def carrito_con(inventario, producto, cantidad):
    c = Carrito(inventario)
    c.agregar(producto, cantidad)
    return c
