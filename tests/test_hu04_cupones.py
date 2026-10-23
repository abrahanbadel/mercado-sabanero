from datetime import date

import pytest

from mercado_sabanero.cupones import Cupon, validar_cupon
from mercado_sabanero.errores import CuponInvalidoError
from mercado_sabanero.cupones import validar_cupon


def test_sabanero10_con_subtotal_minimo_da_diez_por_ciento():
      assert validar_cupon("SABANERO10", 50_000).porcentaje == 10


def test_enviogratis_marca_envio_gratis():
      assert validar_cupon("ENVIOGRATIS", 10_000).envio_gratis is True

def test_sabanero10_bajo_el_minimo_se_rechaza():
      with pytest.raises(CuponInvalidoError):
          validar_cupon("SABANERO10", 49_999)


def test_cupon_inexistente_lanza_error_de_cupon_invalido():
      with pytest.raises(CuponInvalidoError):
          validar_cupon("NOEXISTE", 100_000)


def test_cupon_vencido_lanza_error_de_cupon_invalido():
      catalogo = {"VIEJO": Cupon("VIEJO", porcentaje=10, vence=date(2026, 1, 1))}
      with pytest.raises(CuponInvalidoError):
          validar_cupon("VIEJO", 100_000, hoy=date(2026, 6, 1), catalogo=catalogo)


def test_codigo_de_cupon_no_distingue_mayusculas():
      assert validar_cupon("sabanero10", 50_000).codigo == "SABANERO10"