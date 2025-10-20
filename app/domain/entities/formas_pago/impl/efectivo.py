from ..forma_pago import FormaPago
from ...cajas import Provision, Movimiento


class Efectivo(FormaPago):
    def __init__(self, valor: float):
        super().__init__("Efectivo", valor)

    def procesar_pago(self, provision: Provision, movimiento: Movimiento):
        super().procesar_pago(provision, movimiento)