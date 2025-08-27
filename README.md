# Piedra, Papel o Tijera — Proyecto Integrador (Semanas 1–8)

> **Asignatura:** lógica de programación  
> **Tema marco del proyecto:** *El impacto de las nuevas tecnologías en la sociedad: visualización del futuro.*  

## Datos 
- **Nombre:** _[Angel Iñiguez]_   
- **Fecha:** _[26/08/2025]_  

## Objetivo del programa
Desarrollar el juego **Piedra, Papel o Tijera** que integre los conocimientos vistos en clase: **entrada/salida**, **variables**, **operadores y decisiones**, **estructuras repetitivas**, **listas** y **funciones**

## Funcionalidades principales
- Selección de jugada por parte del usuario con una **validación** (solo acepta `piedra`, `papel` o `tijera`).
- Selección aleatoria de la **CPU**.
- Determinación de **victoria / derrota / empate** .
- **Estadísticas** al finalizar (partidas, victorias, derrotas, empates).
- Uso de **funciones** con parámetros y valores de retorno para modularidad.
- Documentación con **docstrings** y comentarios.

## Relación con los temas / semanas

- **Entrada/Salida (I/O):** `input(...)`, `print(...)`.
- **Variables :** contadores `victorias`, `derrotas`, `empates`, `partidas`.
- **Estructuras de decisión:** `if / elif / else` para evaluar ganador.
- **Estructuras repetitivas:** `while True` para repetir rondas; validación con `while ... not in ...`; `break` para terminar.
- **Estructuras de datos:** **lista** `opciones = ["piedra", "papel", "tijera"]`; uso con `in` y `random.choice(opciones)`.
- **Funciones:**  
  - `pedir_jugada(opciones)` → solicita y **valida** la jugada.  
  - `generar_cpu(opciones)` → elige jugada de la CPU y la muestra.  
  - `decidir_resultado(jugador, CPU)` → retorna `"victoria"`, `"derrota"` o `"empate"`.  
  - `preguntar_continuar()` → retorna `True/False` según la respuesta del usuario.  
  - `mostrar_estadisticas(partidas, victorias, derrotas, empates)` → imprime resumen final.  

## Cómo ejecutar
**Requisitos:** Python 3.8 o mas 

1. Descarga el archivo `piedra_papel_tijera.py` 
2. Abre **PowerShell** y navega a esa carpeta donde este el archivo:
   ```powershell
   cd "C:\Users\usuario\carpeta de la ubicacion"
   ```
3. Ejecuta (usa el nombre real del archivo si es distinto):
   ```powershell
   py piedra_papel_tijera.py

## Pruebas rápidas sugeridas
1. **Entrada válida**: escribir `piedra` → ver jugada CPU → resultado.  
2. **Entrada inválida**: escribir `x` → debe pedir nuevamente hasta que sea válida.  
3. **Varias rondas**: jugar 3–4 veces, luego responder `no` para ver **estadísticas**.  
