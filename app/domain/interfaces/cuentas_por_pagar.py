from datetime import date

from ..entities.asociados import Asociado
from ..entities.cxp import CuentaPorPagar, AbonoCXP
from ..entities.formas_pago import FormaPago


class OperacionesCXP:
    def crear_cuenta_por_pagar(self, asociado: Asociado, comprobante: str, valor: float, fecha: date = date.today()) -> CuentaPorPagar:
        cxp = CuentaPorPagar(comprobante, valor, valor, fecha)
        cxp.asignar_identificacion(asociado)
        return cxp
    
    def registrar_abono(self, cxp: CuentaPorPagar, comprobante: str, formas_pago: list[FormaPago], fecha: date = date.today()) -> AbonoCXP:
        if cxp is None:
            raise Exception("La cuenta por pagar no existe")
        
        abono = AbonoCXP(comprobante, fecha)
        abono.formas_pago = formas_pago
        
        cxp.abonar_cuenta_por_pagar(abono)
        
        return abono
    

operaciones_cxp = OperacionesCXP()