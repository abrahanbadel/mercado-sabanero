from dataclasses import dataclass
from enum import Enum

from .errores import ProductoInvalidoError

TARIFAS_IVA = (0, 5, 19)


class Categoria(Enum):
    ESTANDAR = "ESTANDAR"
    ORO = "ORO"


@dataclass(frozen=True)
class Producto:
    sku: str
    nombre: str
    precio: int
    tarifa_iva: int

    def __post_init__(self):
        if self.precio <= 0:
            raise ProductoInvalidoError("El precio debe ser mayor que cero")
        if self.tarifa_iva not in TARIFAS_IVA:
            raise ProductoInvalidoError("La tarifa de IVA debe ser 0, 5 o 19")

@dataclass(frozen=True)
class LineaCarrito:
    producto: Producto
    cantidad: int

    @property
    def valor(self) -> int:
        return self.producto.precio * self.cantidad
