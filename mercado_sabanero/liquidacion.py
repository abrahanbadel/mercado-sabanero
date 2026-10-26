from fractions import Fraction

from .cupones import validar_cupon
from .descuentos import porcentaje_descuento_volumen
from .modelos import Categoria, Liquidacion
from .redondeo import redondear_peso


def liquidar(carrito, municipio, categoria=Categoria.ESTANDAR,
               codigo_cupon=None, hoy=None) -> Liquidacion:
      subtotal = sum(l.valor for l in carrito.lineas())
      pct = porcentaje_descuento_volumen(subtotal)
      if codigo_cupon:
          pct = max(pct, validar_cupon(codigo_cupon, subtotal, hoy).porcentaje)
      descuento = redondear_peso(subtotal * Fraction(pct, 100))
      return Liquidacion(subtotal, descuento, 0, 0, 0, 0)