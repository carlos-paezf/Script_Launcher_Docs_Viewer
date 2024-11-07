# Organizador de Archivos

Este script automatiza el proceso de mover archivos entre carpetas en función de patrones específicos en sus nombres. Utiliza expresiones regulares para identificar archivos con sufijos de lote y los clasifica en carpetas de "antes del lote" o "después del lote", según corresponda.

## Funcionalidades

- **Clasificación de Archivos:** Identifica y clasifica archivos con patrones específicos de nombres (`"ab"`).
- **Validación de Duplicados:** Si un archivo ya existe en la carpeta destino, el script renombra el archivo duplicado con un sufijo para evitar sobrescrituras.
- **Registro de Movimientos:** Genera un log (`log.txt`) con detalles sobre cada archivo procesado, incluyendo sus rutas de origen y destino.
- **Recursividad en Subcarpetas:** Procesa todas las subcarpetas del directorio de origen, organizando archivos en carpetas específicas por lotes.

## Requisitos

- Python 3.x
- Módulos estándar de Python (`os`, `re`, `shutil`, `time`, `timedelta`)

## Uso

1. Coloca este script en el directorio raíz donde se encuentran las carpetas y archivos a procesar.
2. Ejecuta el script desde el terminal.
3. El script creará una carpeta `OPXBAK` donde organizará los archivos en carpetas separadas antes y después del procesamiento por lotes.
4. Los archivos ya procesados se moverán a una carpeta `Completed`.

## Mejoras Posibles

- **Opciones de Entrada:** Permitir al usuario especificar la carpeta de origen y destino en lugar de asumir el directorio actual.
- **Configuración de Log:** Hacer el nombre del archivo de log y su ubicación configurables.
- **Patrones Dinámicos:** Permitir que el usuario defina los patrones de lote (como `"ab"`) a través de variables de configuración o entrada de usuario.

## Descripción de los Métodos

### `move_file(file, source_path, before_batch_destination_folder, after_batch_destination_folder)`

Mueve un archivo a la carpeta de "antes del lote" o "después del lote", según si el nombre del archivo coincide con el patrón `"ab"`. Registra en `log.txt` detalles sobre el archivo movido.

- Parámetros:
  - `file`: Nombre del archivo a mover.
  - `source_path`: Ruta de origen del archivo.
  - `before_batch_destination_folder`: Carpeta destino para archivos que no coinciden con el patrón.
  - `after_batch_destination_folder`: Carpeta destino para archivos que coinciden con el patrón.

### `validate_duplicated(file, origin, before_batch_destination_folder)`

Verifica si un archivo con el mismo nombre ya existe en la carpeta de "antes del lote". Si el archivo duplicado es más reciente, le agrega el sufijo `"ab"` para diferenciarlo.

- Parámetros:
  - `file`: Nombre del archivo a validar.
  - `origin`: Directorio de origen del archivo.
  - `before_batch_destination_folder`: Carpeta destino para archivos "antes del lote".
- Retorno: La nueva ruta de origen del archivo (renombrado si es necesario).

### `relocate_files(origin, before_batch_destination_folder, after_batch_destination_folder)`

Recorre recursivamente los archivos en `origin`, validando duplicados y moviéndolos a sus respectivas carpetas antes o después del lote.

- Parámetros:
  - `origin`: Directorio de origen para archivos a procesar.
  - `before_batch_destination_folder`: Carpeta destino para archivos antes del lote.
  - `after_batch_destination_folder`: Carpeta destino para archivos después del lote.

## Ejecución

Al ejecutar el script, se muestran los tiempos de ejecución de cada función, ayudando a identificar posibles optimizaciones de tiempo.
