
def filtrar_datos(datos):
    '''
    Prepara los datos de PulseLab para el análisis, reuniendo
    los valores de la señal, los tiempos y la cantidad de hits.

    Parameters
    ----------
    datos : lista

        lista de diccionarios con registros validados del experimento.

    Returns
    -------
    dict
        - diccionario con:
            * "valor": lista de valores de la señal
            * "tiempo": lista de tiempos
            * "hit": cantidad de hits detectados
            * "total_registros": cantidad total de registros.

    '''
    valores = []
    tiempos = []
    hits = 0

    for registro in datos:
        valores.append(registro["valor"])
        tiempos.append(registro["tiempo"])

        if registro["hit"] == 1 or registro["hit"] == "1" or registro["hit"] == True:
            hits += 1

    return {
        "valor": valores,
        "tiempo": tiempos,
        "hit": hits,
        "total_registros": len(datos)
    }
