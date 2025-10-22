from ..asociado import Asociado
from ...servicios import ahorro_educativo


class Independiente(Asociado):
    def agregar_cuenta(self, servicio):
        if servicio == ahorro_educativo:
            raise Exception("El servicio de Ahorro educativo solo está disponible para asociados Cooprokids.")
        
        super().agregar_cuenta(servicio)