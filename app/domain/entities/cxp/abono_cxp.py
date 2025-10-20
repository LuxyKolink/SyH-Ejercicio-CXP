from datetime import date

from ..formas_pago import FormaPago


class AbonoCXP:
    def __init__(self, comprobante: str, fecha: date = date.today()):
        self.fecha = fecha
        self.valor = self.calcular_valor()
        self.comprobante = comprobante
        self.formas_pago: list[FormaPago] = []

    def calcular_valor(self) -> float:
        return sum(forma_pago.valor for forma_pago in self.formas_pago)