from datetime import date

from ..servicios import Servicio
from ..asociados import Asociado


class Cuenta:
    contador_cuentas = 0

    def __init__(self, servicio: Servicio, asociado: Asociado):
        self.servicio = servicio
        self.asociado = asociado
        self.numero = Cuenta.asginar_numero_cuenta(self.servicio)
        self.fecha_apertura: date = date.today()
        self.saldo: float = 0.00

    @classmethod
    def asginar_numero_cuenta(cls, servicio: Servicio) -> str:
        codigo_servicio = servicio.identificador   # '001'

        servicio.contador_servicios += 1
        consecutivo_servicio = str(servicio.contador_servicios).zfill(4)   # '0345' ???

        cls.contador_cuentas += 1
        consecutivo_cuentas = str(cls.contador_cuentas).zfill(4)   # '0001' ???

        return f"{codigo_servicio}{consecutivo_servicio}{consecutivo_cuentas}"
