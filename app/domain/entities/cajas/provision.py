from datetime import date

from .caja import Caja
from .movimiento import Movimiento
from ..formas_pago import Efectivo


class Provision:
    def __init__(self, caja: Caja, valor_inicial: float):
        self.fecha = date.today()
        self.caja = caja
        self.valor_inicial = valor_inicial
        self.movimientos: list[Movimiento] = []

    def calcular_saldo(self) -> Efectivo:
        entradas = sum(movimiento.valor_entrada for movimiento in self.movimientos)
        salidas = sum(movimiento.valor_salida for movimiento in self.movimientos)

        return Efectivo(self.valor_inicial + entradas - salidas)
    
    def permite_retirar(self, monto: float) -> bool:
        saldo_efectivo = self.calcular_saldo()
        return monto <= saldo_efectivo.valor
    
    def agregar_movimiento(self, movimiento: Movimiento):
        movimiento.provision = self
        self.movimientos.append(movimiento)
 