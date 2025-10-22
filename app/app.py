from .domain.entities.servicios import aportes, ahorro_vista, fondo_mutual, ahorro_educativo, ahorro_vivienda
from .domain.entities.asociados import Asociado, Dependiente, Independiente, Cooprokids
from .domain.entities.cajas import Caja
from .domain.entities.formas_pago import FormaPago, Efectivo, Cheque, TrasladoCuenta, Transferencia
from .domain.interfaces import operaciones_caja, operaciones_cxp


def ejecucion():

    # Activar servicios
    aportes.activar_servicio()
    ahorro_vista.activar_servicio()
    fondo_mutual.activar_servicio()
    ahorro_educativo.activar_servicio()
    ahorro_vivienda.activar_servicio()

    # Creación asociados
    dependiente1 = Dependiente("Almejandra", 35, 1005117025)
    dependiente2 = Dependiente("Juan Pablo", 41, 1006154109)

    independiente1 = Independiente("Angelik", 29, 1002183057)

    cooprokids1 = Cooprokids("Diego", 15, 1001953918)
    cooprokids2 = Cooprokids("Santiago", 23, 1005289730)

    asociados: list[Asociado] = [
        dependiente1,
        dependiente2,
        independiente1,
        cooprokids1,
        cooprokids2
    ]

    print(dependiente1.estado)

    for asociado in asociados:
        asociado.activar_asociado()
        for cuenta in asociado.cuentas:
            print(cuenta.numero)

    # Creación Cajas
    caja_bucaramanga = Caja("Caja BU")

    provision = operaciones_caja.aperturar_caja(caja_bucaramanga, 2000000.00)
    print(provision.calcular_saldo())

    # -------------------------------------------------------------------

    # Formas de pago
    formas_pago: list[FormaPago] = []

    efectivo = Efectivo(30000.00)
    formas_pago.append(efectivo)

    movimiento = operaciones_caja.realizar_retiro(provision, formas_pago)
    print(movimiento.comprobante)

    formas_pago.clear()


    # Prueba 2
    cheque = Cheque(200000.00, "1123U", "NU")
    transferencia = Transferencia(50000.00, "237555", "Bancolombia")

    formas_pago.append(cheque)
    formas_pago.append(transferencia)

    movimiento2 = operaciones_caja.realizar_retiro(provision, formas_pago)
    print(movimiento2.comprobante)
    print(provision.calcular_saldo())

    for fp in movimiento2.formas_pago:
        print(fp.valor)