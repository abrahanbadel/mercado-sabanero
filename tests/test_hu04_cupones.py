from mercado_sabanero.cupones import validar_cupon


def test_sabanero10_con_subtotal_minimo_da_diez_por_ciento():
      assert validar_cupon("SABANERO10", 50_000).porcentaje == 10


def test_enviogratis_marca_envio_gratis():
      assert validar_cupon("ENVIOGRATIS", 10_000).envio_gratis is True