from .errores import CantidadInvalidaError, StockInsuficienteError
from .modelos import LineaCarrito, Producto

MIN_UNIDADES = 1
MAX_UNIDADES = 50


class Carrito:
    """Carrito de compras. El inventario es un servicio externo inyectado."""

    def __init__(self, inventario):
        self._inventario = inventario
        self._cantidades: dict[str, int] = {}
        self._productos: dict[str, Producto] = {}

    def agregar(self, producto: Producto, cantidad: int) -> None:
        if not MIN_UNIDADES <= cantidad <= MAX_UNIDADES:
            raise CantidadInvalidaError(
                f"La cantidad debe estar entre {MIN_UNIDADES} y {MAX_UNIDADES}"
            )
        nueva = self._cantidades.get(producto.sku, 0) + cantidad
        if self._inventario.stock_disponible(producto.sku) < nueva:
            raise StockInsuficienteError("Stock insuficiente")
        self._cantidades[producto.sku] = nueva
        self._productos[producto.sku] = producto

    def lineas(self) -> list[LineaCarrito]:
        return [
            LineaCarrito(self._productos[sku], cant)
            for sku, cant in self._cantidades.items()
        ]

    def cantidad_de(self, sku: str) -> int:
        return self._cantidades.get(sku, 0)

    def esta_vacio(self) -> bool:
        return not self._cantidades
