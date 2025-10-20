from datetime import date

from .cuenta import Cuenta
from ..formas_pago import FormaPago


class Extracto:
    def __init__(self, valor_entrada: float, valor_salida: float, comprobante: str):
        self.valor_entrada = valor_entrada
        self.valor_salida = valor_salida
        self.comprobante = comprobante
        self.fecha = date.today()
        self.cuenta: Cuenta = None
        self.formas_pago: list[FormaPago] = []