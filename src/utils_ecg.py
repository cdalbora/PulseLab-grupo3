def detectar_picos_qrs(tiempos: list, senal: list, umbral: float = 0.9, distancia_minima: float =
0.3) -> list:

    '''
   Detecta picos en la señal ECG.
   Parámetros:
          - tiempos: lista de tiempos
          - senal: lista de valores de la señal
          - umbral: valor mínimo para considerar un pico
          - distancia_minima: tiempo mínimo entre picos
  Retorna:
      - lista de tiempos donde ocurren los picos
   '''
    if not senal or not tiempos:
        return []
 
    valor_maximo = max(senal)
    umbral_absoluto = umbral * valor_maximo
 
    picos = []
    ultimo_pico_tiempo = None
 
    for i in range(1, len(senal) - 1):
        es_pico_local = senal[i] > senal[i - 1] and senal[i] > senal[i + 1]
        supera_umbral = senal[i] >= umbral_absoluto
 
        if es_pico_local and supera_umbral:
            if ultimo_pico_tiempo is None or (tiempos[i] - ultimo_pico_tiempo) >= distancia_minima:
                picos.append(tiempos[i])
                ultimo_pico_tiempo = tiempos[i]
 
    return picos

