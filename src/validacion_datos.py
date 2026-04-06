def validar_registro(registro, claves):
    '''
    verifica que cada diccionario dentro de 'claves':
    
    1. Exista dentro de 'registro'
    2. Contenga los campos obligatorios
    3. Que cada campo tenga el tipo correcto:
    
    - "id_participante" → int
    - "tiempo" → str
    - "valor" → str
    - "fase" → str
    - "condicion_experimental" → str
    - "hit" → str

    Return:
        True si todo es válido
        False si alguna condición no se cumple
    '''

    for clave in claves:
        if clave not in registro:
            return False

    for diccionario in claves:

        id_participante = diccionario["id_participante"]
        try:
            id_participante + 0
        except:
            return False

        tiempo = diccionario["tiempo"]
        try:
            tiempo + ""
        except:
            return False

        valor = diccionario["valor"]
        try:
            valor + ""
        except:
            return False

        fase = diccionario["fase"]
        try:
            fase + ""
        except:
            return False

        condicion = diccionario["condicion_experimental"]
        try:
            condicion + ""
        except:
            return False

        hit = diccionario["hit"]
        try:
            hit + ""
        except:
            return False

    return True