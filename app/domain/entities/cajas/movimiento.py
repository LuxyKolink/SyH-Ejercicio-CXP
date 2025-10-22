from __future__ import annotations
from typing import TYPE_CHECKING

from ..formas_pago import FormaPago

if TYPE_CHECKING:
    from .provision import Provision

class Movimiento:
    contador_movimientos = 1

    def __init__(
            self, 
            valor_entrada: float, 
            valor_salida: float, 
            comprobante: str,
        ):
        Movimiento.contador_movimientos += 1
        self.valor_entrada = valor_entrada
        self.valor_salida = valor_salida
        self.comprobante = comprobante
        self.provision: Provision = None
        self.formas_pago: list[FormaPago] = [] 

    @classmethod
    def obtener_consecutivo(cls) -> int:
        return cls.contador_movimientos