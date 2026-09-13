# Una estructura de datos en acción

## Nombre de la aplicación: 

- Inventario de Mochila de Supervivencia en un videojuego

## Descripción no técnica del problema: 
-se necesita implementar una mochila con una cantidad limitada de espacios para llevar sus objetos de supervivencia. Cada objeto debe ocupar una casilla específica. Si la mochila está llena y el jugador encuentra un nuevo objeto, no puede guardarlo a menos que decida soltar o reemplazar uno de los que ya tiene. El programa debe permitir ver qué hay en la mochila, agregar un objeto si hay espacio libre, eliminar un aobjeto que ya no se requiera o avisar si ya no cabe nada más.

## Descripción de la solución: 

-Un programa desarrollado en Python que simula la gestión de una mochila de 4 espacios. Utiliza un arreglo estático inicializado con valores vacíos (None) para controlar las casillas. El sistema cuenta con lógica para mostrar el inventario actual, buscar el primer espacio libre para agregar un nuevo objeto, y eliminar objetos cambiando su posición a vacía cuando el jugador lo requiera.

## Estructura de datos seleccionada:

-Vector o Arreglo (Array) de tamaño estricto fijo

## Justificación técnica de la elección:

- Organización y almacenamiento: Los datos se guardan de forma secuencial en posiciones fijas (índices del 0 al 3). Cada índice representa un "slot" o ranura específica dentro de la mochila.
- Control de disponibilidad: El programa identifica que una casilla está vacía cuando contiene un valor nulo (null) u ocupada cuando ya almacena el nombre de un objeto.
- Acceso y operaciones: El acceso a cualquier objeto es directo si se conoce su posición. La inserción se realiza buscando la primera posición libre y asignándole el objeto, mientras que la eliminación consiste en cambiar el valor de esa posición a null.
- Ventajas: Representa de forma realista la limitación física de una mochila, ocupa un espacio de memoria contiguo y predecible, y es muy eficiente en cuanto a rendimiento porque no requiere reestructuraciones complejas.
- Limitaciones: Su tamaño es estricto; si la mochila tiene 4 espacios, bajo ninguna circunstancia se podrá guardar un quinto objeto, obligando al usuario a liberar espacio primero asi simulando un espacio fisico real.

## Análisis de lo que ocurriría al utilizar otra estructura: 

-Estructura alternativa propuesta: Una Pila (Stack) implementada mediante un vector (comportamiento LIFO).

¿Qué pasaría si la usáramos?: La mochila perdería su flexibilidad de posiciones independientes. Solo podríamos agregar o retirar el último elemento que entró, quedando los demás elementos bloqueados en el fondo.

Comparación clave:

Organización de los datos: El vector permite gestionar casillas independientes (del 0 al 3) donde cada objeto vive en su propio espacio; la pila obliga a que los elementos se apilen uno encima del otro, permitiendo interactuar únicamente con el "tope".

Acceso a los elementos: En el vector podemos consultar o modificar cualquier slot directamente por su índice; en la pila no hay acceso directo al centro o al fondo sin antes desapilar los elementos superiores.

Operaciones de inserción/eliminación: El vector permite insertar, reemplazar o eliminar en cualquier posición libre; la pila restringe estrictamente estas operaciones al último elemento agregado.

Idoneidad para el problema: El vector es ideal para una mochila de videojuego porque un jugador necesita usar o soltar elementos específicos sin importar el orden en que los recolectó. Usar una pila arruinaría la jugabilidad, ya que forzaría una dinámica de "último en entrar, primero en salir" que no aplica para la gestión libre de un inventario.

## Instrucciones para ejecutar el programa: 

1. Abre tu entorno de desarrollo (como Visual Studio Code) y asegúrate de tener instalado Python.
2. Abre la terminal integrada en la carpeta del proyecto.
3. Ejecuta el archivo utilizando la ruta de tu intérprete configurado o mediante el comando correspondiente de tu entorno:
   ```bash
   python mochila.py

## Casos de prueba utilizados: 

Caso 1 (Estado Inicial / Vacío): Se inicializa el arreglo con 4 espacios en None y se ejecuta mostrar_inventario(), verificando que la consola imprima todos los slots como vacíos.

Caso 2 (Funcionamiento Normal / Llenado secuencial): Se agregan cuatro objetos de manera consecutiva ("Arma", "Linterna", "Curas", "Alimentos"), comprobando que cada uno ocupe su respectivo índice del 0 al 3.

Caso 3 (Caso Límite / Desbordamiento): Con el inventario lleno, si se intenta agregar un quinto objeto ("Mapa"). El sistema valida la capacidad, detiene la inserción y arroja el mensaje de error correspondiente sin alterar los datos previos.

Caso 4 (Eliminación y recuperación de espacio): Con el inventario lleno y el quinto objeto bloqueado, se ejecuta quitar_objeto("Linterna") para liberar su ranura, transformándola nuevamente en None. Posteriormente, se reintenta agregar el "Mapa", comprobando que el sistema detecta el espacio libre y realiza la inserción de manera exitosa.

## Limitaciones y posibles mejoras: 

- **Limitación:** El tamaño fijo de 4 elementos restringe la escalabilidad si el jugador adquiere una mejora de almacenamiento en el juego.
- **Posible mejora:** Implementar una función de redimensionamiento dinámico o permitir la creación de una mochila con capacidad variable basada en parámetros de inicialización.

## Enlace al video: 
- https://fumcc-my.sharepoint.com/:v:/g/personal/johansebastiancedenollanten_fumc_edu_co/IQAEjLkrC42tRr0deF3fiIKhAU1O89vQf_1mqgjv-avZkWo?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=sJyspb