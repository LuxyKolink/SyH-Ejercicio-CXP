from ..forma_pago import FormaPago


class Cheque(FormaPago):
    def __init__(self, valor: float, numero_cheque: str, banco: str):
        super().__init__("Cheque")
        self.valor = valor
        self.numero_cheque = numero_cheque
        self.banco = banco