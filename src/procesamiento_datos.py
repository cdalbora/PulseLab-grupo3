import pandas as pd

def filtrar_datos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra el DataFrame conservando solo las columnas necesarias para
    el análisis (tiempo y valor) y agrega una columna con el total de hits.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los registros validados del experimento.

    Returns
    -------
    pd.DataFrame
        DataFrame con las columnas 'tiempo' y 'valor', ordenado por tiempo,
        con el índice reseteado.
    """
    df_filtrado = df[["tiempo", "valor"]].copy()
    df_filtrado = df_filtrado.sort_values("tiempo").reset_index(drop=True)
    return df_filtrado