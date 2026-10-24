from fractions import Fraction

from .redondeo import redondear_peso


def calcular_iva(lineas, porcentaje_descuento: int = 0) -> int:
    """IVA de cada línea sobre su valor ya con el descuento aplicado."""
    factor = Fraction(100 - porcentaje_descuento, 100)
    return sum(
        redondear_peso(l.valor * factor * Fraction(l.producto.tarifa_iva, 100))
        for l in lineas
    )
