from datetime import date

from ..cajas import Caja


class Provision:
    def __init__(self, caja: Caja, valor_inicial: float):
        self.fecha = date.today()
        self.caja = caja
        self.valor_inicial = valor_inicial
