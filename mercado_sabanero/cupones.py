from dataclasses import dataclass


@dataclass(frozen=True)
class Cupon:
      codigo: str
      porcentaje: int = 0
      envio_gratis: bool = False


def validar_cupon(codigo, subtotal):
      if codigo == "SABANERO10":
          return Cupon(codigo, porcentaje=10)
      if codigo == "ENVIOGRATIS":
          return Cupon(codigo, envio_gratis=True)