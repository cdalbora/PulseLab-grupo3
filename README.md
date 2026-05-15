# PulseLab-grupo3

Integrantes: Martiniano Sar, Martina Sergi, Victoria Gaal, Camila D'Albora

Proyecto PulseLab: Procesa datos de señales fisiológicas (ECG) obtenidas en un experimento, con el objetivo de extraer métricas básicas como el promedio de la señal y la frecuencia cardíaca.

MANEJO DE ERRORES
ValueError: para cálculos de promedios, ya que no se puede dividir por cero; para validar que haya como minimo 2 registros de latidos para poder calcular frecuencia



**OBJETOS:**

* **carga\_datos.py:** Para este programa, podríamos implementar una clase llamada "Participante" con un único método \_\_init\_\_ y con los atributos "id\_participante", "tiempo", "valor", "fase", "condicion\_experimental" y "hit".
* **métricas.py:** Usaríamos una clase llamada "RegistroECG" con atributos "tiempo" y "valores". Los métodos serían promedio\_senal(self) y frecuencia\_cardiaca(self).
* **procesamiento\_datos.py:** La clase sería "Experimento", con def \_\_init\_\_(self, registros): y los métodos serían filtrar(), contar\_hits(), obtener\_valores() y obtener\_tiempos().
* **validacion\_datos.py:** En este programa, la clase "Registro" incluiría los atributos "id\_participante", "tiempo", "valor", "fase", "condicion\_experimental" y "hit".Su único método sería def es\_valido().

Funciones que habría que modificar

carga_datos.py: es la que más cambiaría. Todo el proceso de lectura, parseo y conversión de tipos se reemplaza por una sola instrucción de pandas.
validacion_datos.py: la validación de tipos y valores se haría sobre el dataset completo en lugar de registro por registro.
procesamiento_datos.py: el filtrado de valores y el conteo de hits se simplifica con operaciones directas de pandas.
main.py: el filtrado por ID de participante se reduce a una línea.

Funciones que no cambiarían
metricas.py y utils_ecg.py trabajan sobre listas de valores numéricos, por lo que no requerirían modificaciones.