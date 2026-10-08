# Casos de prueba ejecutados

Cada prueba inicia una ejecución nueva con el vector original.

| Prueba | Entradas | Resultado esperado | Resultado obtenido | Coincide |
|---|---|---|---|---|
| 1. Estadísticas iniciales | `3, 5` | Promedio: 75.20; máximo: 92; mínimo: 58; 3 aprobados y 2 reprobados. | Promedio: 75.20; máximo: 92; mínimo: 58; 3 aprobados y 2 reprobados. | Sí |
| 2. Consulta por índice | `2, 2, 5` | Carlos tiene 92 puntos. | Carlos tiene 92 puntos. | Sí |
| 3. Modificación y recálculo | `4, 1, 80, 3, 5` | Vector [85, 80, 92, 74, 58]; promedio 77.80; 4 aprobados y 1 reprobado. | Vector [85, 80, 92, 74, 58]; promedio 77.80; 4 aprobados y 1 reprobado. | Sí |
| 4. Índice inexistente | `2, 5, 0, 5` | Se rechaza el índice 5 y se permite consultar el índice 0. | Se rechaza el índice 5 y se permite consultar el índice 0. | Sí |
| 5. Entrada no numérica y nota inválida | `4, 1, texto, 101, 70, 3, 5` | Se rechazan texto y 101; se acepta 70; promedio 75.80; 4 aprobados. | Se rechazan texto y 101; se acepta 70; promedio 75.80; 4 aprobados. | Sí |
| 6. Límite de aprobación | `4, 1, 70, 3, 5` | Luis aprueba con 70; promedio 75.80; 4 aprobados y 1 reprobado. | Luis aprueba con 70; promedio 75.80; 4 aprobados y 1 reprobado. | Sí |

Registros completos: `evidencias/prueba_1.txt` a `prueba_6.txt`.
