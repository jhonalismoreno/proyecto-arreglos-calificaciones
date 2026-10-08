# Sistema de calificaciones con arreglos y vectores

**Estudiante:** Jhonalis Pérez Moreno  
**Asignatura:** Introducción a la Programación - ITLA  
**Actividad:** Capítulo IX: Arreglos y vectores

## Descripción
Programa de consola que administra las calificaciones de cinco estudiantes
utilizando listas de Python como vectores unidimensionales.

## Objetivo
Aplicar la creación, consulta, modificación y recorrido de un vector,
combinando índices, ciclos, condiciones y cálculos.

## Lenguaje y requisitos
Python 3. No requiere librerías externas.

## Funcionalidades
- Mostrar cinco notas y el estado de cada estudiante.
- Consultar una nota por su índice (0 a 4).
- Calcular promedio, máximo y mínimo.
- Contar aprobados y reprobados mediante un ciclo y una condición `if`.
- Modificar una nota y mostrar el vector actualizado.
- Validar opciones, índices y notas enteras entre 0 y 100.

Para este ejercicio se aprueba con una nota de 70 o más. Es una regla del
proyecto, no una afirmación sobre la política académica de una institución.
Las modificaciones se mantienen durante la ejecución; al reiniciar se
restablece el vector inicial. No se utiliza una base de datos.

## Instrucciones para ejecutar
1. Instalar Python 3 y descargar los archivos del repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

```bash
python main.py
```

En macOS o Linux también puede utilizarse `python3 main.py`.
En Windows puede utilizarse `py main.py`.
4. Elegir una opción del menú y seguir las indicaciones.
5. Utilizar la opción 5 para salir.

## Ejemplo de resultados iniciales
Vector: `[85, 67, 92, 74, 58]`.
Promedio: **75.20**. Máximo: **92**. Mínimo: **58**.
Aprobados: **3**. Reprobados: **2**.
Al modificar el índice 1 a 80, el vector queda `[85, 80, 92, 74, 58]`,
el promedio es **77.80**, con **4 aprobados** y **1 reprobado**.

## Archivos
- `main.py`: código fuente completo.
- `README.md`: descripción e instrucciones.
- `casos_de_prueba.md`: datos, resultados esperados y obtenidos.
- `evidencias/`: imágenes fieles del código y de salidas reales de ejecución,
  junto con el registro de la sesión. Las imágenes se presentan como
  registros visuales; no simulan capturas de una computadora del estudiante.

## Fuentes
- https://docs.python.org/es/3/tutorial/introduction.html#lists
- https://docs.python.org/es/3/tutorial/controlflow.html
- https://docs.python.org/es/3/library/functions.html
- https://docs.python.org/es/3/library/exceptions.html#IndexError
