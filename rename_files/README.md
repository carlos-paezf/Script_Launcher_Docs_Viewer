# Rename Files and Folders Script

## Descripción

Este script permite renombrar archivos y carpetas en un directorio específico y sus subdirectorios, eliminando caracteres especiales y acentos según las opciones configuradas. Su propósito es limpiar los nombres para facilitar la compatibilidad entre sistemas y mejorar la organización.

## Funcionalidades

- **Renombrado de archivos y carpetas**: Elimina espacios, caracteres especiales y acentos en nombres de archivos y carpetas.
- **Parámetros opcionales**: Permite configurar si se desea eliminar acentos y caracteres especiales.
- **Ejecución recursiva**: Recorrer y renombrar archivos y carpetas en subdirectorios.

## Requisitos

- Python 3.x
- Librería `unidecode` (instalable mediante `pip install unidecode` o con el comando `pip install -r requirements.txt`)

## Uso

1. Colocar el script en una ubicación accesible.
2. Ejecutar el script en la terminal:

    ```bash
    python script.py
    ```

3. Ingresar la ruta del directorio que se desea procesar cuando se solicite.
4. El script renombrará todos los archivos y carpetas en el directorio indicado, eliminando caracteres especiales y acentos.

## Mejoras Posibles

- Agregar manejo de excepciones para evitar errores en casos de permisos de archivo o nombres duplicados.
- Permitir al usuario elegir si se renombrarán archivos, carpetas o ambos.
- Añadir opción para previsualizar los cambios sin aplicar el renombrado.

## Descripción de los Métodos en el Código

### `clean_name(name, remove_accent_marks=False, remove_special_characters=False) -> str`

Limpia el nombre del archivo o carpeta según las opciones de limpieza configuradas.

- Parámetros:
  - `name`: Nombre original del archivo o carpeta.
  - `remove_accent_marks`: (bool) Elimina marcas de acento si es True.
  - `remove_special_characters`: (bool) Elimina caracteres especiales si es True.
- Retorno: Devuelve el nombre limpiado en formato de texto.

### `rename_files_and_folders(root, remove_accent_marks=False, remove_special_characters=False)`

Renombra archivos y carpetas en el directorio raíz especificado y sus subdirectorios aplicando las opciones de limpieza.

- Parámetros:
  - `root`: Ruta del directorio raíz.
  - `remove_accent_marks`: (bool) Elimina marcas de acento en nombres si es True.
  - `remove_special_characters`: (bool) Elimina caracteres especiales en nombres si es True.

## Ejecución Principal

- Solicita al usuario la ruta del directorio raíz.
- Configura las opciones de limpieza (`remove_accent_marks` y `remove_special_characters` en True).
- Calcula el tiempo de ejecución y lo imprime al finalizar.

Este repositorio contiene un script de Python que renombra archivos y carpetas dentro de un directorio raíz especificado. El script permite limpiar los nombres de archivos y carpetas eliminando espacios, acentos y caracteres especiales según las opciones especificadas.
