from abc import ABC


class FormaPago(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre
