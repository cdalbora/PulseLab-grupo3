
def calcular_promedio_senal(datos):
    '''
    Calcula el promedio de la señal ECG de un participante

    Parameters
    ----------
    datos : diccionario
      Diccionario que contiene la información del participante,
      incluyendo la clave "valor", que es una lista de valores de la señal ECG.


    Returns
    -------
    promedio: float
    El valor promedio de la señal. 
    
    Raises
    -------
    ValueError: si la lista esta vacia

    '''
    valores= datos["valor"]
    suma=0
    promedio=0
    if len(valores) == 0:
        raise ValueError("Lista vacía")
    else:
        suma=sum(valores)
        promedio=suma/len(valores)
    return promedio 
    
def calcular_frecuencia_cardiaca(picos):
    '''
    Toma la lista de los tiempos donde se dieron los picos (latidos); si hay al 
    menos 2 picos(no se puede calcular frecuencia con un solo dato) calcula cuantos latidos 
    hubo por minuto a partir de la cantidad de latidos y cuanto tiempo paso entre el primer
    y el ultimo pico
                                                                             
    Parameters
    ----------
    picos : list
        Lista de tiempos donde se dieron los picos de los latidos

    Returns
    -------
    frecuencia: float
        La cantidad de latidos por minuto 
    
    Raises
    --------
    ValueError: si hay menos de 2 latidos registrados o si el tiempo total es 0
    '''
    if len(picos) < 2:
        raise ValueError("No se puede calcular frecuencia de menos de 2 latidos")
    tiempo_total = picos[-1] - picos[0]
    cantidad_latidos = len(picos)
    
    if tiempo_total == 0:
        raise ValueError("Tiempo total invalido")
    
    frecuencia = (cantidad_latidos / tiempo_total) * 60
    return frecuencia
    
from src.utils_ecg import detectar_picos_qrs
def calcular_fc_desde_datos(datos):
    tiempos = []
    senal = []
    for d in datos:
        tiempos.append(d["tiempo"])
        senal.append(d["valor"])
    picos = detectar_picos_qrs(tiempos, senal)
    return calcular_frecuencia_cardiaca(picos)