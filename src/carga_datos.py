def parsear_linea(linea):
    """
     Parsea los datos de una linea, separa los campos y los guarda en una lista.

    Parameters
    ----------
    
    linea : str
        Datos correspondientes al experimento.

    Returns
    -------
    list: lista con los valores convertidos (id_participante, tiempo, valor, fase, condicion_experimental, hit).
    """
    linea = linea.strip("\n")
    partes = linea.split(",")
    
    id_participante = int(partes[0])
    tiempo = float(partes[1])
    valor = float(partes[2])
    fase = str(partes[3])
    condicion_experimental = str(partes[4])
    hit = int(partes[5])
    
    return [id_participante, tiempo, valor, fase, condicion_experimental, hit] 


def cargar_datos(ruta):
    """
    Recorre las lineas del archivo descargado, las parsea y genera un diccionario con los datos de cada participante.

    Parameters
    ----------
    ruta : str
        Ruta del archivo con los datos del experimento.

    Returns
    -------
    list: lista de diccionarios, donde cada diccionario representa un participante con sus datos.  

    """
    arch_datos = open(ruta, "r")
    lista_lineas = arch_datos.readlines()
    arch_datos.close()
    
    datos_totales = []
    
    for linea in lista_lineas:
        datos = parsear_linea(linea)
        datos_totales.append(datos)
        
    datos_dict = {}
    
    for dato in datos_totales:
        id_p, tiempo, valor, fase, cond_exp, hit = dato 
        
        if id_p not in datos_dict:
            datos_dict[id_p] = { "id_participante":id_p,
            "tiempo": [],
            "valor": [],
            "fase": [],
            "condicion_experimental": [],
            "hit": []
            }   

        datos_dict[id_p]["tiempo"].append(tiempo)
        datos_dict[id_p]["valor"].append(valor)
        datos_dict[id_p]["fase"].append(fase)
        datos_dict[id_p]["condicion_experimental"].append(cond_exp) 
        datos_dict[id_p]["hit"].append(hit)
                
    return list(datos_dict.values())
                
    
    
        
        