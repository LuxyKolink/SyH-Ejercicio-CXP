from ..forma_pago import FormaPago
from ...cajas import Provision, Movimiento


class Transferencia(FormaPago):
    def __init__(self, valor: float, numero_cta_bancaria: str, banco: str):
        super().__init__("Transferencia", valor)
        self.numero_cta_bancaria = numero_cta_bancaria
        self.banco = banco

    def procesar_pago(self, provision: Provision, movimiento: Movimiento):
        super().procesar_pago(provision, movimiento)
