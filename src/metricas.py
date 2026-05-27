import pandas as pd
from src.utils_ecg import detectar_picos_qrs


def calcular_promedio_senal(df: pd.DataFrame) -> float:
    """
    Calcula el promedio de la señal ECG.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame que contiene la columna 'valor'.

    Returns
    -------
    float
        Valor promedio de la señal.

    Raises
    ------
    ValueError
        Si el DataFrame está vacío.
    """
    if df.empty:
        raise ValueError("El DataFrame está vacío, no se puede calcular el promedio")
    return float(df["valor"].mean())


def calcular_frecuencia_cardiaca(picos: list) -> float:
    """
    Calcula la frecuencia cardíaca en latidos por minuto a partir de
    los tiempos de los picos detectados.

    Parameters
    ----------
    picos : list
        Lista de tiempos donde se detectaron picos R.

    Returns
    -------
    float
        Frecuencia cardíaca en latidos por minuto.

    Raises
    ------
    ValueError
        Si hay menos de 2 picos o si el tiempo total es 0.
    """
    if len(picos) < 2:
        raise ValueError("No se puede calcular la frecuencia con menos de 2 latidos")

    tiempo_total = picos[-1] - picos[0]
    if tiempo_total == 0:
        raise ValueError("Tiempo total inválido (igual a 0)")

    frecuencia = (len(picos) / tiempo_total) * 60
    return frecuencia


def calcular_fc_desde_datos(df: pd.DataFrame) -> float:
    """
    Detecta picos QRS en la señal y calcula la frecuencia cardíaca.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con columnas 'tiempo' y 'valor'.

    Returns
    -------
    float
        Frecuencia cardíaca en latidos por minuto.
    """
    tiempos = df["tiempo"].tolist()
    senal = df["valor"].tolist()
    picos = detectar_picos_qrs(tiempos, senal)
    return calcular_frecuencia_cardiaca(picos)