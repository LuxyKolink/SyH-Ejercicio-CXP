from enum import Enum


class EstadoServicio(Enum):
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"


class Servicio:
    contador_servicios: int = 0

    def __init__(self, identificador: str, nombre: str):
        self.identificador = identificador
        self.nombre = nombre
        self.estado = EstadoServicio.INACTIVO

    def activar_servicio(self):
        self.estado = EstadoServicio.ACTIVO

aportes = Servicio('001', "Aportes")
fondo_mutual = Servicio('002',"Fondo mutual")
ahorro_vista = Servicio('003', "Ahorro a la vista")
ahorro_educativo = Servicio('010', "Ahorro educativo")
ahorro_vivienda = Servicio('016', "Ahorro vivienda")
