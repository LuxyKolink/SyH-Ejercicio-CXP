from ..forma_pago import FormaPago
from ...cuentas import Cuenta


class TrasladoCuenta(FormaPago):
    def __init__(self, valor: float, cuenta: Cuenta):
        super().__init__("Traslado de Cuenta")
        self.valor = valor
        self.cuenta = cuenta