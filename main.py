"""Sistema de calificaciones - Capítulo IX: Arreglos y vectores.
Estudiante: Jhonalis Pérez Moreno.
"""

NOTA_APROBACION = 70  # Regla elegida para este ejercicio.


def leer_entero(mensaje, minimo, maximo):
    """Solicita un entero válido dentro de un intervalo."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"Ingrese un valor entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada inválida. Escriba un número entero.")


def mostrar_calificaciones(nombres, calificaciones):
    print("\nVECTOR:", calificaciones)
    for indice in range(len(calificaciones)):
        nota = calificaciones[indice]
        if nota >= NOTA_APROBACION:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        print(f"[{indice}] {nombres[indice]}: {nota} - {estado}")


def calcular_estadisticas(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    aprobados = 0
    reprobados = 0
    for nota in calificaciones:
        if nota >= NOTA_APROBACION:
            aprobados += 1
        else:
            reprobados += 1
    return promedio, max(calificaciones), min(calificaciones), aprobados, reprobados


def mostrar_estadisticas(calificaciones):
    promedio, mayor, menor, aprobados, reprobados = calcular_estadisticas(calificaciones)
    print(f"\nPromedio: {promedio:.2f}")
    print(f"Calificación más alta: {mayor}")
    print(f"Calificación más baja: {menor}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")


def main():
    nombres = ["Ana", "Luis", "Carlos", "María", "Pedro"]
    calificaciones = [85, 67, 92, 74, 58]
    print("SISTEMA DE CALIFICACIONES")
    print("Capítulo IX - Arreglos y vectores")
    print(f"Se aprueba con {NOTA_APROBACION} puntos o más.")
    mostrar_calificaciones(nombres, calificaciones)

    while True:
        print("\n1. Mostrar calificaciones")
        print("2. Consultar por índice")
        print("3. Mostrar estadísticas")
        print("4. Modificar una calificación")
        print("5. Salir")
        opcion = leer_entero("Seleccione una opción: ", 1, 5)

        if opcion == 1:
            mostrar_calificaciones(nombres, calificaciones)
        elif opcion == 2:
            indice = leer_entero("Índice a consultar (0-4): ", 0, len(calificaciones) - 1)
            print(f"{nombres[indice]} tiene {calificaciones[indice]} puntos.")
        elif opcion == 3:
            mostrar_estadisticas(calificaciones)
        elif opcion == 4:
            indice = leer_entero("Índice a modificar (0-4): ", 0, len(calificaciones) - 1)
            nueva_nota = leer_entero("Nueva calificación (0-100): ", 0, 100)
            anterior = calificaciones[indice]
            calificaciones[indice] = nueva_nota
            print(f"Nota de {nombres[indice]} modificada: {anterior} -> {nueva_nota}")
            mostrar_calificaciones(nombres, calificaciones)
        else:
            print("\nVECTOR FINAL:", calificaciones)
            print("Programa finalizado correctamente.")
            break


if __name__ == "__main__":
    main()
