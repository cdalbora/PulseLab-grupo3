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





**IMPLEMENTACIÓN CON PANDAS**

**Funciones que fueron modificadas**

* **carga\_datos.py:** es la que más cambió. En lugar de recorrer el archivo línea por línea, convertir cada campo manualmente y armar diccionarios, pandas lee el archivo completo de una sola vez y construye la tabla automáticamente.
* **validacion\_datos.py:** antes se validaba cada registro uno por uno. Ahora la validación se hace sobre todos los datos a la vez, lo que simplifica bastante el código.
* **procesamiento\_datos.py:** el filtrado y el conteo de hits se simplificaron, aprovechando que pandas permite hacer operaciones sobre columnas enteras directamente en lugar de recorrer los registros con un loop.
* **metricas.py:** el cálculo del promedio y la preparación de los datos para detectar picos se adaptaron para trabajar con la nueva estructura de tabla en lugar de listas y diccionarios.
* **main.py:** el filtrado por participante se simplificó. Además se agregó la creación automática de la carpeta donde se guardan los gráficos, y dos funciones nuevas que generan y guardan las visualizaciones al finalizar el análisis.



**Función que no cambió**

* **utils\_ecg.py:** su lógica trabaja directamente sobre valores numéricos, por lo que no necesitó ninguna modificación.





**Guía de Ejecución de la Interfaz Web**



1. Para correr el dashboard interactivo, abrir el buscador de Windows, buscar y abrir cmd. Una vez abierto, ejecutar el siguiente comando reemplazando las rutas por las de su computadora:
"C:\\ruta\\a\\python.exe" -m streamlit run "C:\\ruta\\a\\tu\\proyecto\\app.py"

2. Para encontrar la ruta de Python correcta, abrir Spyder y ejecutar en la consola:
python
import sys
print(sys.executable)

3. Copiar el resultado y usarlo como primera ruta. La segunda ruta es simplemente la ubicación de app.py en su computadora.

4. Una vez ejecutado el comando, presionar Enter cuando pregunte por el email y el navegador se abrirá automáticamente con la aplicación. Si no abre solo, copiar http://localhost:8501 en el navegador.

* **Si Streamlit no está instalado, antes de correr el dashboard se debe ejecutar**

&#x20;  **"C:\\ruta\\a\\python.exe" -m pip install streamlit**



