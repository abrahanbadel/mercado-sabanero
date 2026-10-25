from fractions import Fraction
from math import floor


def redondear_peso(valor: Fraction) -> int:
    """Redondea al peso más cercano (mitades hacia arriba)."""
    return floor(valor + Fraction(1, 2))
