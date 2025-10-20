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

    def abonar_cuenta_por_pagar(self, abono: AbonoCXP):
        if abono.fecha < self.fecha:
            raise Exception("La fecha de los abonos no debe ser inferior a la fecha de la CxP.")
        
        suma_abonos = sum(abono.valor for abono in self.abonos) + abono.valor

        if suma_abonos > self.saldo:
            raise Exception("La sumatoria de los abonos no debe superar el saldo pendiente.")
        
        self.abonos.append(abono)

    def calcular_saldo_actual(self) -> float:
        suma_abonos = sum(abono.valor for abono in self.abonos)
        return self.saldo - suma_abonos
