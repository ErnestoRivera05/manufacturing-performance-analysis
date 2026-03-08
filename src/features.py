import pandas as pd


def cal_yield(df, col_producidas, col_defectos):
    yield_series = (df[col_producidas] - df[col_defectos]) / df[col_producidas]

    yield_series = yield_series.replace(
        [float("inf"), -float("inf")], 0
    )  # Si hay un número raro, le pone 0
    yield_series = yield_series.fillna(0)  # Si existe un Nan, le pone 0
    yield_series = yield_series.clip(0, 1)  # Permite un rango entre 0 y 1

    return yield_series


def cal_scrap(df, col_defectos, col_unidades_producidas):
    scrap_rate = df[col_defectos] / df[col_unidades_producidas]
    scrap_rate = scrap_rate.replace(
        [float("inf"), -float("inf")], 0
    )  # si el resultado de la division es inf o -inf lo reemplaza por 0
    scrap_rate = scrap_rate.fillna(0)  # Si existe un Nan, le pone 0
    scrap_rate = scrap_rate.clip(0, 1)  # resultado es entre 0 y 1
    return scrap_rate


def cal_productividad(df, col_unidades_producidas, col_horas_trabajadas):

    productividad = df[col_unidades_producidas] / df[col_horas_trabajadas]

    productividad = productividad.replace([float("inf"), -float("inf")], 0)
    productividad = productividad.fillna(0)
    productividad = productividad.clip(
        lower=0
    )  # recorda los valores para que no existan negativos
    # En productividad no tiene sentido que existan valores negativos

    return productividad


def calc_disponibilidad(df, col_trabajo, col_mant):
    disp = df[col_trabajo] / (df[col_trabajo] + df[col_mant])

    disp = disp.replace([float("inf"), -float("inf")], 0)
    disp = disp.fillna(0)
    disp = disp.clip(0, 1)

    return disp


def calc_rendimiento(df, col_productividad, produc_objetivo):
    produc_objec = df[col_productividad] / produc_objetivo
    return produc_objec
