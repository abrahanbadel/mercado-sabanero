from mercado_sabanero.liquidacion import liquidar
from mercado_sabanero.modelos import Categoria

def test_ejemplo_del_enunciado(carrito, licuadora, cafe, arroz):
      carrito.agregar(licuadora, 1)
      carrito.agregar(cafe, 2)
      carrito.agregar(arroz, 4)

      res = liquidar(carrito, "Sincelejo", Categoria.ESTANDAR)

      assert (res.subtotal, res.descuento, res.iva) == (228_000, 11_400, 33_915)
      assert (res.envio, res.total, res.puntos) == (0, 250_515, 250)


def test_puntos_no_incluyen_el_envio(carrito, cafe):
      carrito.agregar(cafe, 2)  # total 39.500 con envío 8.000 -> puntos sobre 31.500
      assert liquidar(carrito, "Sincelejo").puntos == 31