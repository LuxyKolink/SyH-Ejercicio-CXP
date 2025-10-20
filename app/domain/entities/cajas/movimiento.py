from .provision import Provision
from ..formas_pago import FormaPago


class Movimiento:
    def __init__(
            self, 
            valor_entrada: float, 
            valor_salida: float, 
            comprobante: str,
        ):
        self.valor_entrada = valor_entrada
        self.valor_salida = valor_salida
        self.comprobante = comprobante
        self.provision: Provision = None
        self.formas_pago: list[FormaPago] = [] 

    def puede_retirar(self, monto: float) -> bool:
        if self.provision is None:
            return False
        saldo_efectivo = self.provision.saldo_efectivo()
        return monto <= saldo_efectivo
