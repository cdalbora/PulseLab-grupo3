**Descripción del Sistema**

PulseLab es una aplicación de análisis de señales ECG obtenidas en un experimento de laboratorio. El sistema procesa los datos de cada participante, calcula métricas cardíacas y presenta los resultados a través de una interfaz web interactiva.



**Arquitectura Modular**

El sistema está organizado en módulos independientes dentro de la carpeta src/:



* carga\_datos.py: lee el archivo CSV del experimento y devuelve un DataFrame validado con los datos de todos los participantes.
* validacion\_datos.py: verifica que el DataFrame contenga todas las columnas requeridas, que los tipos sean correctos y que no haya valores negativos.
* procesamiento\_datos.py: filtra el DataFrame conservando las columnas necesarias para el análisis (tiempo y valor), ordenadas cronológicamente.
* metricas.py: calcula el promedio de la señal ECG y la frecuencia cardíaca en latidos por minuto a partir de los picos detectados.
* utils\_ecg.py: detecta los picos QRS de la señal ECG usando un umbral relativo al valor máximo y una distancia mínima entre picos.





**Interfaz Web (app.py)**

La interfaz está construida con Streamlit y sigue el siguiente flujo:



* El usuario sube el archivo CSV mediante un componente de carga de archivos
* El sistema valida el archivo y muestra un error si los datos son inválidos, bloqueando el avance
* El usuario selecciona un participante específico o elige ver todos
* Se muestran 4 indicadores clave: promedio de señal, frecuencia cardíaca, cantidad de hits y total de registros
* Se muestran dos gráficos: la señal ECG con los picos QRS marcados, y un gráfico de barras con los hits por fase





Estructura de Directorios

PulseLab/

├── app.py

├── src/

│   ├── carga\_datos.py

│   ├── validacion\_datos.py

│   ├── procesamiento\_datos.py

│   ├── metricas.py

│   ├── utils\_ecg.py

│   └── diseño.md

├── graficos/

└── datos/

&#x20;   └── PulseLab\_mock\_data.csv

├── README



**Tecnologías utilizadas**

* pandas: lectura, validación y procesamiento de datos tabulares
* matplotlib: generación de gráficos
* streamlit: interfaz web interactiva
* pathlib: creación automática de directorios

