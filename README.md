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

