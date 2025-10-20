from ..asociado import Asociado
from ...servicios import ahorro_educativo


class Dependinte(Asociado):
    def agregar_cuenta(self, cuenta):
        if cuenta.servicio == ahorro_educativo:
            raise Exception("El servicio de Ahorro educativo solo está disponible para asociados Cooprokids.")
        
        super().agregar_cuenta(cuenta)