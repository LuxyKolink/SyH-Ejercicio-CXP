from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from ..cajas import Provision, Movimiento


class FormaPago(ABC):
    def __init__(self, nombre: str, valor: float):
        self.nombre = nombre
        self.valor = valor

    @abstractmethod
    def procesar_pago(self, provision: Provision, movimiento: Movimiento):        
        if provision is None:
            raise Exception("No existe una provisión de caja.")
        
        movimiento.formas_pago.append(self)
