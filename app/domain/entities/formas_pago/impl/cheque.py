from ..forma_pago import FormaPago
from ...cajas import Provision, Movimiento


class Cheque(FormaPago):
    def __init__(self, valor: float, numero_cheque: str, banco: str):
        super().__init__("Cheque", valor)
        self.numero_cheque = numero_cheque
        self.banco = banco

    def procesar_pago(self, provision: Provision, movimiento: Movimiento):
        super().procesar_pago(provision, movimiento)
