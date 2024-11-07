# Script de Actualización de Contenido de Interfaces

## Descripción

Este script permite procesar archivos de un directorio, seleccionándolos por extensiones válidas y palabras clave en sus nombres. Los archivos seleccionados se procesan para generar versiones actualizadas en un directorio de destino, aplicando reglas específicas para la escritura de cada tipo de archivo.

## Funcionalidades

- **Selección de archivos**: Filtra archivos en el directorio fuente por extensiones válidas y palabras clave (`ISEC`, `IFXD`, `ICUS`).
- **Procesamiento de archivos**: Lee cada archivo seleccionado y lo guarda en el directorio de destino con líneas modificadas según el tipo de archivo.
- **Decorador de tiempo de ejecución**: Mide el tiempo de ejecución de las funciones clave para optimización y monitoreo de rendimiento.

## Requisitos

- Python 3.x
- Acceso a los directorios de archivos de entrada y salida

## Uso

1. Colocar el script en una ubicación accesible.
2. Ejecutar el script desde la terminal:

    ```bash
    python script.py
    ```

3. Ingresar las rutas de los directorios de origen y destino cuando se solicite.
4. El script seleccionará y procesará los archivos, generando copias actualizadas en el directorio de destino.

## Mejoras Posibles

- Agregar manejo de excepciones para errores en permisos de archivo o nombres duplicados.
- Permitir al usuario personalizar las palabras clave (ISEC, IFXD, ICUS) y las extensiones válidas.
- Implementar un sistema de log para registrar los archivos procesados y los errores encontrados.

## Descripción de los Métodos en el Código

### `measure_run_time(func)`

Un decorador para medir el tiempo de ejecución de funciones específicas.

- Parámetros:
  - `func`: La función cuyo tiempo de ejecución se desea medir.

- Retorno: La función wrap, que ejecuta la función y calcula el tiempo transcurrido.

### `get_files()`

Obtiene una lista de archivos en el directorio de origen (SEARCH_DIR) que cumplen con las extensiones válidas y contienen una de las interfaces especificadas (ISEC, IFXD, ICUS).

- Retorno: Lista de nombres de archivos que cumplen los criterios especificados.

### `process_files(files: list[str])`

Procesa cada archivo en la lista files, determinando el tipo de archivo y aplicando el procesamiento correspondiente.

- Parámetros:
  - `files`: Lista de nombres de archivos que cumplen los criterios de filtrado.
- Acciones: Crea las carpetas de destino si no existen, lee cada archivo, y llama a `write_lines` con el número de repeticiones de comas adecuado.

### `write_lines(original_lines: list[str], final_file: str, n_repetitions: int)`

Escribe cada línea de un archivo, añadiendo una cantidad específica de comas al final.

- Parámetros:
  - `original_lines`: Lista de líneas de texto del archivo original.
  - `final_file`: Ruta del archivo de destino donde se escribirán las líneas procesadas.
  - `n_repetitions`: Número de comas que se añaden al final de cada línea en el archivo de destino.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado.
3. Puede generar el archivo `.exe`siguiendo estos pasos:
   1. Instalar la librería `pyinstaller` con el siguiente comando `pip install pyinstaller`
   2. Generar el ejecutable con el comando `pyinstaller --onefile main.py`
   3. Encontrar el archivo en la carpeta `dist`
