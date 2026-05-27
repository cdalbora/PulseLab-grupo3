import pandas as pd
from src.validacion_datos import validar_dataframe

COLUMNAS = ["id_participante", "tiempo", "valor", "fase", "condicion_experimental", "hit"]


def cargar_datos(ruta: str) -> pd.DataFrame:
    """
    Lee el archivo CSV del experimento y devuelve un DataFrame validado.

    Parameters
    ----------
    ruta : str
        Ruta al archivo CSV con los datos del experimento.

    Returns
    -------
    pd.DataFrame
        DataFrame con las columnas: id_participante, tiempo, valor,
        fase, condicion_experimental, hit.

    Raises
    ------
    ValueError
        Si el archivo tiene una cantidad de columnas incorrecta,
        valores negativos, o tipos de datos inválidos.
    KeyError
        Si falta alguna columna obligatoria.
    """
    df = pd.read_csv(ruta, header=None, names=COLUMNAS)

    df["id_participante"] = df["id_participante"].astype(int)
    df["tiempo"] = df["tiempo"].astype(float)
    df["valor"] = df["valor"].astype(float)
    df["fase"] = df["fase"].astype(str).str.strip()
    df["condicion_experimental"] = df["condicion_experimental"].astype(str).str.strip()
    df["hit"] = df["hit"].astype(str).str.strip().map({"True": 1, "False": 0}).astype(int)

    validar_dataframe(df)

    return df
                
    
    
        
        