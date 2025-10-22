from ..asociado import Asociado
from ...servicios import ahorro_educativo


class Cooprokids(Asociado):
    def agregar_cuenta(self, servicio):
        if servicio != ahorro_educativo:
            raise Exception("Un asociado Cooprokids solo puede tener adicional una cuenta de Ahorro educativo.")
        
        super().agregar_cuenta(servicio)
