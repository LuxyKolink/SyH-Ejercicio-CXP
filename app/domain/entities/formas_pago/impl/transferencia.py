from ..forma_pago import FormaPago


class Transferencia(FormaPago):
    def __init__(self, valor: float, numero_cta_bancaria: str, banco: str):
        super().__init__("Transferencia")
        self.valor = valor
        self.numero_cta_bancaria = numero_cta_bancaria
        self.banco = banco
