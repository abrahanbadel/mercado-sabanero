from fractions import Fraction

from .cupones import validar_cupon
from .descuentos import porcentaje_descuento_volumen
from .envio import calcular_envio
from .iva import calcular_iva
from .modelos import Categoria, Liquidacion
from .puntos import calcular_puntos
from .redondeo import redondear_peso


def liquidar(carrito, municipio, categoria=Categoria.ESTANDAR,
               codigo_cupon=None, hoy=None) -> Liquidacion:
      lineas = carrito.lineas()
      subtotal = sum(l.valor for l in lineas)
      pct = porcentaje_descuento_volumen(subtotal)
      envio_gratis = False
      if codigo_cupon:
          cupon = validar_cupon(codigo_cupon, subtotal, hoy)
          pct = max(pct, cupon.porcentaje)  # no se suman: aplica el mayor
          envio_gratis = cupon.envio_gratis

      descuento = redondear_peso(subtotal * Fraction(pct, 100))
      iva = calcular_iva(lineas, pct)
      envio = calcular_envio(municipio, subtotal - descuento + iva, envio_gratis)
      total = subtotal - descuento + iva + envio
      puntos = calcular_puntos(total - envio, categoria)
      return Liquidacion(subtotal, descuento, iva, envio, total, puntos)