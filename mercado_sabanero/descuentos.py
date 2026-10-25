UMBRAL_5 = 200_000
UMBRAL_10 = 500_000


def porcentaje_descuento_volumen(subtotal: int) -> int:
    if subtotal >= UMBRAL_10:
        return 10
    if subtotal >= UMBRAL_5:
        return 5
    return 0