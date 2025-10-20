from ..forma_pago import FormaPago


class Efectivo(FormaPago):
    def __init__(self, valor: float):
        super().__init__("Efectivo")
        self.valor = valor