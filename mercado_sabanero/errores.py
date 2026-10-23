class ErrorDeNegocio(Exception):
    """Base de los errores de reglas de negocio."""


class CantidadInvalidaError(ErrorDeNegocio):
    """La cantidad a agregar debe estar entre 1 y 50 unidades."""


class StockInsuficienteError(ErrorDeNegocio):
    """No hay unidades suficientes en el inventario."""


class CuponInvalidoError(ErrorDeNegocio):
    """El cupón no existe, está vencido o no cumple el mínimo."""


class CarritoVacioError(ErrorDeNegocio):
    """No se puede liquidar un carrito sin productos."""


class ProductoInvalidoError(ErrorDeNegocio):
    """Datos de producto no válidos (precio o tarifa de IVA)."""
