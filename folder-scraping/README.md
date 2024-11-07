# Folder Scraping

## Descripción

Este script genera un informe detallado en formato Excel sobre los archivos en un directorio base específico. El informe incluye metadatos como tamaño, fecha de modificación y una serie de etiquetas para clasificar cada archivo (ej., si es un log, backup, pdf, etc.). Se utilizan varias funciones para verificar palabras clave en el nombre de archivos y determinar el tipo de archivo basándose en sus extensiones y patrones específicos.

## Funcionalidades

1. **Definir directorios de entrada y salida** (`define_io_paths`): Solicita al usuario el directorio base y el de destino para el archivo Excel.
2. **Obtención de metadatos de archivos** (`get_files_info`): Recorre el directorio base y extrae información de cada archivo según las extensiones permitidas.
3. **Clasificación de archivos** (`get_metadata`): Clasifica archivos según etiquetas específicas (ej., relacionado con auditoría, contingencia, capacitación, etc.) y verifica su validez.
4. **Exportación a Excel**: Guarda el reporte de archivos en un archivo Excel en la ruta especificada por el usuario.

## Requisitos

- Python 3.6+
- Bibliotecas `pandas`, `os`, `re`, y `datetime` (incluidas en la biblioteca estándar de Python, excepto `pandas`, que se debe instalar).
  
## Uso

1. **Ejecutar el script**: Ejecutar el script para iniciar el proceso. Se pedirá ingresar el directorio base y la ruta de destino para guardar el archivo Excel.
2. **Especificar extensiones**: Si se requiere, definir extensiones específicas de archivo en `allowed_extensions` (actualmente permite todas las extensiones).
3. **Salida del informe**: El archivo Excel generado incluirá columnas con información detallada sobre cada archivo en el directorio base, incluyendo su tamaño, fecha de modificación y etiquetas de clasificación.

### Ejecución

Para usar el script, sigue estos pasos:

1. Configura el directorio base (`base_directory`) en el que quieres analizar los archivos.
2. Configura la ruta del archivo Excel (`excel_file_path`) donde se guardarán los resultados del análisis.
3. Opcionalmente, puedes definir un conjunto de extensiones permitidas para filtrar los archivos que se analizarán.
4. Ejecuta el script escribiendo `python script.py`.
5. Los resultados del análisis se guardarán en el archivo Excel especificado.

Este script está diseñado para analizar archivos en un directorio específico y recopilar metadatos sobre ellos. También proporciona la capacidad de filtrar archivos por su extensión y realizar ciertas comprobaciones sobre los nombres de archivo y las rutas.

## Mejoras posibles

- Filtrar extensiones: Agregar la posibilidad de definir extensiones permitidas al inicio del script para personalizar el análisis.
- Validación de entrada de usuario: Verificar que las rutas ingresadas sean válidas y existan.
- Opciones de salida: Permitir otros formatos de salida, como CSV o JSON.
- Registros detallados: Agregar registros detallados de ejecución para fines de auditoría y depuración.

## Descripción de los Métodos en el Código

### `is_valid_name(name: str) -> bool`

- Descripción: Verifica si un nombre de archivo cumple con el patrón de caracteres alfanuméricos y guiones bajos.
- Parámetros:
  - `name` (nombre del archivo).
- Retorno: True o False según el cumplimiento del patrón.

### `check_keywords(string: str, keywords: set) -> bool`

- Descripción: Verifica si alguna palabra clave está presente en el string.
- Parámetros:
  - `string` (texto donde buscar).
  - `keywords` (conjunto de palabras clave).
- Retorno: True o False según la presencia de alguna palabra clave.

### `check_keywords_in_path_and_file(path: str, file: str, keywords: set) -> bool`

- Descripción: Verifica si alguna palabra clave está presente en la ruta o el nombre del archivo.
- Parámetros:
  - `path` (directorio del archivo).
  - `file` (nombre del archivo).
  - `keywords` (conjunto de palabras clave).
- Retorno: True o False según la presencia de alguna palabra clave.

### `file_has_allowed_extension(file: str, allowed_extensions: set) -> bool`

- Descripción: Verifica si el archivo tiene una extensión permitida.
- Parámetros:
  - `file` (nombre del archivo).
  - `allowed_extensions` (conjunto de extensiones permitidas).
- Retorno: True o False según el cumplimiento de la extensión.

### `get_metadata(current_folder: str, file: str, path: str)`

- Descripción: Obtiene metadatos y clasificaciones del archivo, incluyendo tamaño, fecha de modificación y etiquetas.
- Parámetros:
  - `current_folder` (directorio actual).
  - `file` (nombre del archivo).
  - `path` (directorio base).
- Retorno: Tupla con información del archivo.

### `get_files_info(path: str, allowed_extensions: set = None)`

- Descripción: Recopila metadatos de los archivos en el directorio base y filtra por extensiones permitidas.
- Parámetros:
  - `path` (directorio base).
  - `allowed_extensions` (extensiones permitidas).
- Retorno: Lista de diccionarios con la información de cada archivo.

### `define_io_paths() -> str`

- Descripción: Solicita al usuario el directorio base y de destino para generar la ruta de salida del archivo Excel.
- Retorno: Ruta del directorio base y del archivo Excel de salida.
