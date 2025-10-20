from datetime import date

from ..asociados import Asociado
from .abono_cxp import AbonoCXP


class CuentaPorPagar:
    def __init__(self, comprobante: str, valor: float, saldo: float, fecha: date = date.today()):
        self.fecha = fecha
        self.comprobante = comprobante
        self.valor = valor
        self.saldo = saldo
        self.identificacion: int = None
        self.abonos = list[AbonoCXP] = []

    def asignar_identificacion(self, asociado: Asociado):
        self.identificacion = asociado.identificacion

    def abonar_cuenta_por_pagar(self):
        pass