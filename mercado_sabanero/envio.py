import unicodedata

COSTO_SINCELEJO = 8_000
COSTO_OTROS_MUNICIPIOS = 15_000
UMBRAL_ENVIO_GRATIS = 150_000


def _normalizar(texto: str) -> str:
    sin_tildes = unicodedata.normalize("NFD", texto)
    return "".join(c for c in sin_tildes if unicodedata.category(c) != "Mn").strip().lower()


def calcular_envio(municipio: str, base_con_iva: int, envio_gratis: bool = False) -> int:
    if envio_gratis or base_con_iva >= UMBRAL_ENVIO_GRATIS:
        return 0
    if _normalizar(municipio) == "sincelejo":
        return COSTO_SINCELEJO
    return COSTO_OTROS_MUNICIPIOS
