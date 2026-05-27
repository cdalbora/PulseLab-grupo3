from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_datos
from src.metricas import calcular_promedio_senal, calcular_fc_desde_datos
from src.utils_ecg import detectar_picos_qrs

RUTA_DATOS = "datos/PulseLab_mock_data.csv"
CARPETA_GRAFICOS = Path("graficos")
CARPETA_GRAFICOS.mkdir(exist_ok=True)

def obtener_datos_participante(df: pd.DataFrame, id_participante: int) -> pd.DataFrame:
    """
    Filtra las filas correspondientes a un participante específico.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame completo con todos los registros.
    id_participante : int
        ID del participante a filtrar.

    Returns
    -------
    pd.DataFrame
        Subconjunto del DataFrame con los registros del participante.

    Raises
    ------
    ValueError
        Si no existen registros para ese ID.
    """
    df_participante = df[df["id_participante"] == id_participante]
    if df_participante.empty:
        raise ValueError(
            f"No se encontraron registros para el participante con ID {id_participante}"
        )
    return df_participante.reset_index(drop=True)


def graficar_senal(df_filtrado: pd.DataFrame, picos: list, id_label: str) -> None:
    """
    Genera y guarda un gráfico de la señal ECG con los picos marcados.

    Parameters
    ----------
    df_filtrado : pd.DataFrame
        DataFrame con columnas 'tiempo' y 'valor'.
    picos : list
        Lista de tiempos donde se detectaron picos QRS.
    id_label : str
        Etiqueta para el título y el nombre del archivo.
    """
    fig, ax = plt.subplots(figsize=(12, 4))

    ax.plot(df_filtrado["tiempo"], df_filtrado["valor"],
            color="steelblue", linewidth=0.8, label="Señal ECG")

    if picos:
        df_picos = df_filtrado[df_filtrado["tiempo"].isin(picos)]
        ax.scatter(df_picos["tiempo"], df_picos["valor"],
                   color="crimson", zorder=5, s=40, label="Picos QRS")

    ax.set_title(f"Señal ECG — {id_label}")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Amplitud")
    ax.legend()
    ax.grid(True, alpha=0.3)

    nombre_archivo = f"senal_ecg_{id_label.replace(' ', '_')}.png"
    ruta_salida = CARPETA_GRAFICOS / nombre_archivo
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.show()
    plt.close()
    print(f"Gráfico guardado en: {ruta_salida}")


def graficar_hits_por_fase(df: pd.DataFrame, id_label: str) -> None:
    """
    Genera y guarda un gráfico de barras con la cantidad de hits por fase.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con columnas 'fase' y 'hit'.
    id_label : str
        Etiqueta para el título y el nombre del archivo.
    """
    hits_por_fase = df.groupby("fase")["hit"].sum()

    fig, ax = plt.subplots(figsize=(7, 4))
    hits_por_fase.plot(kind="bar", ax=ax, color="steelblue", edgecolor="white")

    ax.set_title(f"Hits por fase — {id_label}")
    ax.set_xlabel("Fase")
    ax.set_ylabel("Cantidad de hits")
    ax.tick_params(axis="x", rotation=30)
    ax.grid(axis="y", alpha=0.3)

    nombre_archivo = f"hits_por_fase_{id_label.replace(' ', '_')}.png"
    ruta_salida = CARPETA_GRAFICOS / nombre_archivo
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.show()
    plt.close()
    print(f"Gráfico guardado en: {ruta_salida}")

try:
    datos = cargar_datos(RUTA_DATOS)
    id_input = input(
        "¿Querés ver un participante en particular? Ingresá su ID (o Enter para ver todos): "
    ).strip()

    if id_input:
        datos_seleccionados = obtener_datos_participante(datos, int(id_input))
        id_label = f"participante_{id_input}"
    else:
        datos_seleccionados = datos.copy()
        id_label = "todos"

    datos_filtrados = filtrar_datos(datos_seleccionados)

    promedio = calcular_promedio_senal(datos_filtrados)
    frecuencia = calcular_fc_desde_datos(datos_filtrados)
    total_hits = int(datos_seleccionados["hit"].sum())

    print(f"\nPromedio señal:      {promedio:.4f}")
    print(f"Frecuencia cardíaca: {frecuencia:.2f} lpm")
    print(f"Cantidad de hits:    {total_hits}")
    print(f"Total de registros:  {len(datos_seleccionados)}")

    picos = detectar_picos_qrs(
        datos_filtrados["tiempo"].tolist(),
        datos_filtrados["valor"].tolist()
    )
    graficar_senal(datos_filtrados, picos, id_label)
    graficar_hits_por_fase(datos_seleccionados, id_label)

except ValueError as e:
    print(f"Error de valor: {e}")

except KeyError as e:
    print(f"Error de clave: {e}")

except FileNotFoundError:
    print(f"No se encontró el archivo: {RUTA_DATOS}")