from fractions import Fraction

from .cupones import validar_cupon
from .descuentos import porcentaje_descuento_volumen
from .envio import calcular_envio
from .errores import CarritoVacioError
from .iva import calcular_iva
from .modelos import Categoria, Liquidacion
from .puntos import calcular_puntos
from .redondeo import redondear_peso


def _aplicar_cupon(codigo_cupon, subtotal, pct_volumen, hoy):
    """Devuelve (porcentaje, envio_gratis). Los descuentos no se suman: aplica el mayor."""
    if not codigo_cupon:
        return pct_volumen, False
    cupon = validar_cupon(codigo_cupon, subtotal, hoy)
    return max(pct_volumen, cupon.porcentaje), cupon.envio_gratis


def liquidar(carrito, municipio, categoria=Categoria.ESTANDAR,
             codigo_cupon=None, hoy=None) -> Liquidacion:
    lineas = carrito.lineas()
    if not lineas:
        raise CarritoVacioError("El carrito está vacío")

    subtotal = sum(l.valor for l in lineas)
    pct, envio_gratis = _aplicar_cupon(
        codigo_cupon, subtotal, porcentaje_descuento_volumen(subtotal), hoy
    )

    descuento = redondear_peso(subtotal * Fraction(pct, 100))
    iva = calcular_iva(lineas, pct)
    envio = calcular_envio(municipio, subtotal - descuento + iva, envio_gratis)
    total = subtotal - descuento + iva + envio
    puntos = calcular_puntos(total - envio, categoria)
    return Liquidacion(subtotal, descuento, iva, envio, total, puntos)