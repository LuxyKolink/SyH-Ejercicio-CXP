from ..asociado import Asociado
from ...servicios import ahorro_educativo


class Cooprokids(Asociado):
    def agregar_cuenta(self, cuenta):
        if cuenta.servicio != ahorro_educativo:
            raise Exception("Un asociado Cooprokids solo puede tener adicional una cuenta de Ahorro educativo.")
        
        super().agregar_cuenta(cuenta)
