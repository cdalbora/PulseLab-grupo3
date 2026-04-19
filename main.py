from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_datos
from src.metricas import calcular_promedio_senal, calcular_fc_desde_datos

ruta="datos/PulseLab_mock_data.csv"

def obtener_datos_participante(datos, id_participante):
    """
    Filtra los registros de un participante específico por su ID.
 
    Parameters
    ----------
    datos : list
        Lista completa de registros del experimento.
    id_participante : int
        ID del participante a buscar.
 
    Returns
    -------
    list
        Lista de registros que corresponden al participante.
 
    Raises
    ------
    ValueError
        Si no se encuentran registros para ese ID.
    """
    registros = [r for r in datos if r["id_participante"] == id_participante]
    if not registros:
        raise ValueError(f"No se encontraron registros para el participante con ID {id_participante}")
    return registros
 

#1. leer datos desde archivo
try:
    datos = cargar_datos(ruta)
#2 pregunta si se quiere ver los datos de un participante en particular o de todos
    id_input = input("¿Querés ver un participante en particular? Ingresá su ID (o Enter para ver todos): ").strip()
    
    if id_input:
        datos_seleccionados = obtener_datos_participante(datos, int(id_input))
    else:
        datos_seleccionados = datos
#2. Filtrar datos (señal y tiempo)
    datos_filtrados = filtrar_datos(datos_seleccionados)

#3. Detectar picos y calcular métricas

    promedio = calcular_promedio_senal(datos_filtrados)
    frecuencia = calcular_fc_desde_datos(datos_seleccionados)
    
except ValueError as e:
    print(f"Error: {e}")
    
except KeyError as e: 
    print(f"Error: {e}")
    
else:
#4. Mostrar resultados
    print("Promedio señal:", promedio)
    print("Frecuencia cardíaca:", frecuencia)
    print("Cantidad de hits:", datos_filtrados["hit"])

