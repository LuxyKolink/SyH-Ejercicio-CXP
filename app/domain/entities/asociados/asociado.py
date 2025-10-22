from enum import Enum
from abc import ABC, abstractmethod

from ..cuentas import Cuenta
from ..servicios import Servicio, aportes


class EstadoAsociado(Enum):
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    PROCESO_RETIRO = "En proceso de retiro"
    RETIRO = "Retiro"

class Asociado(ABC):
    def __init__(self, nombre: str, edad: int, identificacion: int):
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion
        self.estado = EstadoAsociado.INACTIVO
        self.cuentas: list[Cuenta] = [] 
        self.cuentas.append(Cuenta(aportes, self))

    def activar_asociado(self):
        self.estado = EstadoAsociado.ACTIVO

    @abstractmethod
    def agregar_cuenta(self, servicio: Servicio) -> Cuenta:
        if servicio.estado.value == "Inactivo":
            raise Exception("No se permite crear una cuenta de un servicio inactivo.")
        
        cuenta = Cuenta(servicio, self)
        self.cuentas.append(cuenta)
        return cuenta
    