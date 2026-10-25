from .modelos import Categoria


def calcular_puntos(total_sin_envio: int, categoria: Categoria) -> int:
    puntos = total_sin_envio // 1_000
    return puntos * 2 if categoria is Categoria.ORO else puntos