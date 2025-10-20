from ..entities.cajas import Caja, Provision, Movimiento
from ..entities.formas_pago import FormaPago


PREFIJO_INGRESO = 'I'
PREFIJO_EGRESO = 'E'
SUCURSAL = 'BU'


class Operaciones:
    def aperturar_caja(self, caja: Caja, valor_inicial: float):
        provision = Provision(caja, valor_inicial)
        return provision
    
    def realizar_retiro(self, provision: Provision, formas_pago: list[FormaPago]):
        valor_total = sum(forma_pago.valor for forma_pago in formas_pago)
        if not provision.permite_retirar(valor_total):
            raise Exception("No se permite retiro de dinero si el valor es superior al saldo disponible en Efectivo")
        
        consecutivo_comprobante = str(Movimiento.obtener_consecutivo()).zfill(3)
        comprobante = f"{PREFIJO_EGRESO}{SUCURSAL}{consecutivo_comprobante}"

        movimiento = Movimiento(0.00, valor_total, comprobante)

        for forma_pago in formas_pago:
            forma_pago.procesar_pago(provision, movimiento)

        provision.agregar_movimiento(movimiento)
        

    def realizar_consignacion(self, provision: Provision, formas_pago: list[FormaPago]):
        pass