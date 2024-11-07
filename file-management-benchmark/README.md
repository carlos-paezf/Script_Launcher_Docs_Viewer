# Procesamiento de Archivos en Directorios

## Descripción

Este script procesa archivos de entrada con un formato específico (`GRSSYREY.g0X` donde X varía entre 1 y 9), realiza búsquedas de archivos en un directorio, copia archivos coincidentes a un directorio de destino y genera archivos de salida con las líneas procesadas. También incluye una función para validar la búsqueda de archivos basándose en palabras clave extraídas de cada línea.

## Funcionalidades

1. **Decorador de tiempo de ejecución**: Calcula y muestra el tiempo que tarda en ejecutarse una función.
2. **Procesamiento de archivos** (`process_files`):
   - Lee archivos de entrada, realiza búsquedas basadas en palabras clave y copia archivos coincidentes.
   - Escribe líneas en archivos de salida.
   - Imprime información sobre el número de líneas leídas y escritas.
3. **Validación de código** (`validate_code`): Valida las búsquedas de archivos en el directorio basándose en palabras clave sin escribir en archivos de salida.

## Requisitos

- Python 3.6+
- Biblioteca `shutil` y `os` (incluidas en la biblioteca estándar de Python).
- Directorios específicos:
  - `Z:\OPXGRSS`: Directorio de búsqueda.
  - `Z:\OPXGRSSPROD`: Directorio de destino.
  
## Uso

1. Asegurarse de que los directorios `Z:\OPXGRSS` y `Z:\OPXGRSSPROD` existen y contienen los archivos necesarios.
2. Ejecutar el script con `process_files()` para procesar los archivos o `validate_code()` para solo realizar la validación de búsqueda sin procesar archivos de salida.
3. La salida de tiempo de ejecución se mostrará en consola junto con la información de cada archivo procesado.

### Ejecución

- Ejecutar el procesamiento completo

```python
process_files()
```

- Ejecutar solo la validación de búsqueda

```python
validate_code()
```

## Mejoras posibles

- Manejo de errores: Implementar excepciones para manejar archivos faltantes o rutas incorrectas.
- Parámetros configurables: Permitir que los directorios de entrada y salida se pasen como parámetros en vez de estar codificados.
- Paralelización: Paralelizar el procesamiento para mejorar el rendimiento cuando se manejan grandes volúmenes de datos.
- Salida de registros: Guardar registros en un archivo para un análisis posterior de resultados y errores.

## Descripción de los Métodos en el Código

### `measure_run_time(func)`

- Descripción: Decorador que mide el tiempo de ejecución de una función y lo muestra en la consola.
- Parámetros:
  - `func` (función a ejecutar).
- Retorno: Función envuelta con tiempo de ejecución medido.

### `process_files()`

- Descripción: Procesa archivos de entrada con formato específico, realiza búsquedas de archivos en el directorio de búsqueda, copia los archivos encontrados al directorio de destino, y genera archivos de salida con las líneas correspondientes.
- Parámetros: Ninguno.
- Retorno: Ninguno (Imprime en consola información sobre líneas procesadas).

### `validate_code()`

- Descripción: Valida la búsqueda de archivos en el directorio Z:\OPXGRSS utilizando palabras clave extraídas del archivo GRSSYREY.g07 y muestra archivos coincidentes en consola sin escribir en archivos de salida.
- Parámetros: Ninguno.
- Retorno: Ninguno (Imprime en consola las coincidencias encontradas).
