import matplotlib.pyplot as plt
import streamlit as st

from src.carga_datos import cargar_datos_desde_upload
from src.procesamiento_datos import filtrar_datos
from src.metricas import calcular_promedio_senal, calcular_fc_desde_datos
from src.utils_ecg import detectar_picos_qrs

# ── Configuración de la página ─────────────────────────────────────────────────
st.set_page_config(page_title="PulseLab Dashboard", layout="wide")
st.title("PulseLab — Dashboard ECG")

# ── 1. Carga dinámica de datos ─────────────────────────────────────────────────
archivo = st.file_uploader("Subí el archivo CSV del experimento", type="csv")

if archivo is None:
    st.info("Esperando archivo CSV...")
    st.stop()

# ── 2. Puente de validación defensiva ─────────────────────────────────────────
try:
    df = cargar_datos_desde_upload(archivo)
except ValueError as e:
    st.error(f"Error en los datos: {e}")
    st.stop()
except KeyError as e:
    st.error(f"Columna faltante: {e}")
    st.stop()

# ── Selector de participante ───────────────────────────────────────────────────
ids_disponibles = sorted(df["id_participante"].unique().tolist())
opciones = ["Todos"] + [str(i) for i in ids_disponibles]
seleccion = st.selectbox("Participante", opciones)

if seleccion == "Todos":
    df_seleccionado = df.copy()
    id_label = "Todos los participantes"
else:
    id_participante = int(seleccion)
    df_seleccionado = df[df["id_participante"] == id_participante].reset_index(drop=True)
    id_label = f"Participante {seleccion}"

df_filtrado = filtrar_datos(df_seleccionado)

# ── 3. KPIs ────────────────────────────────────────────────────────────────────
promedio = calcular_promedio_senal(df_filtrado)
frecuencia = calcular_fc_desde_datos(df_filtrado)
total_hits = int(df_seleccionado["hit"].sum())
total_registros = len(df_seleccionado)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Promedio señal", f"{promedio:.4f}")
col2.metric("Frecuencia cardíaca", f"{frecuencia:.1f} lpm")
col3.metric("Hits", total_hits)
col4.metric("Registros", total_registros)

st.divider()

# ── 4. Visualizaciones ─────────────────────────────────────────────────────────
picos = detectar_picos_qrs(
    df_filtrado["tiempo"].tolist(),
    df_filtrado["valor"].tolist()
)

# Gráfico 1: señal ECG con picos
st.subheader(f"Señal ECG — {id_label}")
fig1, ax1 = plt.subplots(figsize=(12, 4))
ax1.plot(df_filtrado["tiempo"], df_filtrado["valor"],
         color="steelblue", linewidth=0.8, label="Señal ECG")
if picos:
    df_picos = df_filtrado[df_filtrado["tiempo"].isin(picos)]
    ax1.scatter(df_picos["tiempo"], df_picos["valor"],
                color="crimson", zorder=5, s=40, label="Picos QRS")
ax1.set_xlabel("Tiempo (s)")
ax1.set_ylabel("Amplitud")
ax1.legend()
ax1.grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig1)
plt.close(fig1)

# Gráfico 2: hits por fase
st.subheader(f"Hits por fase — {id_label}")
hits_por_fase = df_seleccionado.groupby("fase")["hit"].sum()
fig2, ax2 = plt.subplots(figsize=(7, 4))
hits_por_fase.plot(kind="bar", ax=ax2, color="steelblue", edgecolor="white")
ax2.set_xlabel("Fase")
ax2.set_ylabel("Cantidad de hits")
ax2.tick_params(axis="x", rotation=30)
ax2.grid(axis="y", alpha=0.3)
plt.tight_layout()
st.pyplot(fig2)
plt.close(fig2)

