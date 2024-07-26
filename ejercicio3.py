def leer_horas_trabajadas(horas: float) -> float:
    return horas

def leer_tarifa(tarifa: float) -> float:
    return tarifa

def calcular_sueldo(horas: float, tarifa: float) -> float:
    if tarifa <= 0:
        raise Exception("La tarifa debe ser superior a 0")
    if horas > 40.:
        base = 40. * tarifa
        extra = (horas - 40.) * tarifa * 1.5
        return base + extra
    elif 0. <= horas <= 40.:
        return horas * tarifa
    else:
        raise Exception("Las horas trabajadas no pueden ser negativas")

horas = leer_horas_trabajadas(-10)
tarifa = leer_tarifa(20)
sueldo = calcular_sueldo(horas, tarifa)
print(sueldo)