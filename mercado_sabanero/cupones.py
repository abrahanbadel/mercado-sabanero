from dataclasses import dataclass
from datetime import date

from .errores import CuponInvalidoError


@dataclass(frozen=True)
class Cupon:
      codigo: str
      porcentaje: int = 0
      subtotal_minimo: int = 0
      envio_gratis: bool = False
      vence: date | None = None


def validar_cupon(codigo, subtotal, hoy=None, catalogo=None) -> Cupon:
      if catalogo is None:
          catalogo = {
              "SABANERO10": Cupon("SABANERO10", porcentaje=10, subtotal_minimo=50_000),
              "ENVIOGRATIS": Cupon("ENVIOGRATIS", envio_gratis=True),
          }
      hoy = hoy or date.today()
      cupon = catalogo.get((codigo or "").strip().upper())
      if cupon is None:
          raise CuponInvalidoError("Cupón inválido")
      if cupon.vence is not None and hoy > cupon.vence:
          raise CuponInvalidoError("Cupón inválido: vencido")
      if subtotal < cupon.subtotal_minimo:
          raise CuponInvalidoError("Cupón inválido: no alcanza el subtotal mínimo")
      return cupon