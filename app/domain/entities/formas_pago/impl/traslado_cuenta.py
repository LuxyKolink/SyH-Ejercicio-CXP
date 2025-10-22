from __future__ import annotations
from typing import TYPE_CHECKING

from ..forma_pago import FormaPago
from ...cajas import Provision, Movimiento

if TYPE_CHECKING:
    from ...cuentas import Cuenta, Extracto


class TrasladoCuenta(FormaPago):
    def __init__(self, valor: float, cuenta: Cuenta):
        super().__init__("Traslado de Cuenta", valor)
        self.cuenta = cuenta

    def procesar_pago(self, provision: Provision, movimiento: Movimiento):
        if self.cuenta is None:
            raise Exception("Debe especificar la cuenta a la que se hace el traslado.")

        extracto = Extracto(self.valor, 0.00, movimiento.comprobante)
        extracto.cuenta = self.cuenta
        extracto.formas_pago.append(self)

        super().procesar_pago(provision, movimiento)

