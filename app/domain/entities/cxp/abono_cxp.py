from datetime import date

from ..formas_pago import FormaPago


class AbonoCXP:
    def __init__(self, comprobante: str, fecha: date = date.today()):
        self.fecha = fecha
        self.valor = 0.00
        self.comprobante = comprobante
        self.formas_pago: list[FormaPago] = []