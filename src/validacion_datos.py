def validar_registro(registro, claves):
    '''
    verifica que el registro contenga todas las claves requeridas
    y que los valores tengan el tipo esperado:
    
    - "id_participante" → int
    - "tiempo" → float
    - "valor" → float
    - "fase" → str
    - "condicion_experimental" → str
    - "hit" → int
    
    Parameters
    ----------
    registro : dict
        Diccionario que representa un registro individual del experimento,
        con claves como "id_participante", "tiempo", "valor", etc.

    claves : list
        Lista de strings con los nombres de las claves obligatorias
        que el registro debe contener.
        
    Returns 
    ----------
        bool
        True si todo es válido
        False si alguna condición no se cumple
    '''

    for clave in claves:
        if clave not in registro:
            raise KeyError(f"Falta la clave obligatoria: {clave}")
        
    if registro["tiempo"] < 0:
        raise ValueError("El tiempo no puede ser negativo")
    
    if registro["valor"] < 0:
        raise ValueError("El valor no puede ser negativo")
    
    try:
        registro["id_participante"] + 0
        registro["tiempo"] + 0.0
        registro["valor"] + 0.0
        registro["fase"] + ""
        registro["condicion_experimental"] + ""
        registro["hit"] + 0
        
    except TypeError:
        return False

    return True
   