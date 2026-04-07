from carga_datos import cargar_datos
from procesamiento_datos import filtrar_datos
from metricas import calcular_promedio_senal, calcular_fc_desde_datos

#1. leer datos desde archivo
datos = cargar_datos("datos.csv")

#2. Filtrar datos (señal y tiempo)
datos_filtrados = filtrar_datos(datos)

#3. Detectar picos y calcular métricas
promedio = calcular_promedio_senal(datos_filtrados)
frecuencia = calcular_fc_desde_datos(datos)

#4. Mostrar resultados
print("Promedio señal:", promedio)
print("Frecuencia cardíaca:", frecuencia)
print("Cantidad de hits:", datos_filtrados["hit"])

