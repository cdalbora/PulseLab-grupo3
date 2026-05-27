import pandas as pd

TIPOS_ESPERADOS = {
    "id_participante": (int,),
    "tiempo": (float, int),
    "valor": (float, int),
    "fase": (str,),
    "condicion_experimental": (str,),
    "hit": (int,),
}

COLUMNAS_REQUERIDAS = list(TIPOS_ESPERADOS.keys())


def validar_dataframe(df: pd.DataFrame) -> None:
    """
    Valida que el DataFrame contenga todas las columnas requeridas,
    que los tipos sean los esperados y que no haya valores negativos
    en tiempo ni en valor.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los registros del experimento.

    Raises
    ------
    KeyError
        Si falta alguna columna obligatoria.
    ValueError
        Si hay valores negativos en tiempo o valor.
    TypeError
        Si alguna columna tiene un tipo incompatible.
    """
    for col in COLUMNAS_REQUERIDAS:
        if col not in df.columns:
            raise KeyError(f"Falta la columna obligatoria: '{col}'")

    if (df["tiempo"] < 0).any():
        raise ValueError("Hay valores negativos en la columna 'tiempo'")

    if (df["valor"] < 0).any():
        raise ValueError("Hay valores negativos en la columna 'valor'")

    for col, tipos in TIPOS_ESPERADOS.items():
        if not all(isinstance(v, tipos) for v in df[col]):
            raise TypeError(f"La columna '{col}' contiene valores de tipo incorrecto")