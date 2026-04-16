from src.validacion_datos import validar_registro

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
    
    if len(partes) != 6:
        raise ValueError("Cantidad de campos inválida")
        
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
    claves = ["id_participante", "tiempo", "valor", "fase", "condicion_experimental", "hit"]
    
    for linea in lista_lineas:
        #intenta parsear
        try:
            datos = parsear_linea(linea)
        except: 
            continue #si el dato es de tipo incorrecto, lo saltea
        
        registro = {
            "id_participante": datos[0],
            "tiempo": datos[1],
            "valor": datos[2],
            "fase": datos[3],
            "condicion_experimental": datos[4],
            "hit": datos[5]
        }
        #Validar datos antes de añadir el diccionario a la lista de datos general
        if validar_registro(registro, claves):
            datos_totales.append(registro)
    return datos_totales 
                
    
    
        
        