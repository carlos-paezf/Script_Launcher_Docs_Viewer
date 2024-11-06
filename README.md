# Script Launcher - Docs Viewer

Una aplicación de escritorio en Python con interfaz gráfica para ejecutar scripts y visualizar documentación. Permite seleccionar y ejecutar archivos `.py` o `.exe` desde un menú lateral, mientras que su documentación se muestra en formato HTML en la misma ventana.

## Funcionalidades

- *Ejecución de Scripts*: Selecciona y ejecuta scripts Python (.py) o archivos ejecutables (.exe) desde una interfaz intuitiva.
- *Visualización de Documentación*: Muestra la documentación de cada script en formato HTML, extrayéndola desde el archivo `README.md` ubicado en la misma carpeta que el script.
- *Interfaz Gráfica (GUI)*: Creada con Tkinter, incluye un menú lateral para la selección de scripts y un panel principal para visualizar el contenido de README.md.

## Requisitos

Este script requiere Python 3.x y las siguientes bibliotecas:

- `markdown`
- `tkhtmlview`

Puedes instalar las dependencias necesarias ejecutando:

```txt
$: pip install -r requirements.txt
```

## Uso

Para utilizar el script, sigue estos pasos:

1. Clona el repositorio (opcional):

    ```bash
    git clone <https://github.com/carlos-paezf/Script_Launcher_Docs_Viewer.git>
    ```

2. Organización de scripts: Coloca los scripts `.py` o `.exe` en subdirectorios dentro de la ruta especificada en el código (`C:\\Users\\carlo\\Documents\\Python Scripts` en este ejemplo).

3. Visualización de scripts: La aplicación cargará los scripts en el menú lateral mostrando el nombre de la carpeta contenedora de cada uno.

4. Visualización de README.md: Al seleccionar un script, se mostrará su contenido de README.md en el panel de documentación (si existe).

5. Ejecución de scripts: Pulsa el botón "Ejecutar Script" en el panel principal para ejecutar el script seleccionado.

## Estructura del Proyecto

```txt
ScriptLauncher-DocsViewer/
├── main.py          # Código principal de la aplicación
├── README.md        # Instrucciones y documentación de la aplicación
└── [Directorio de Scripts]
    ├── Script1/
    │   ├── script1.py
    │   └── README.md
    └── Script2/
        ├── script2.exe
        └── README.md
```

## Personalización

Para personalizar el comportamiento y la apariencia:

- *Ruta de los scripts*: Cambia la ruta en el método find_scripts dentro de create_sidemenu.
- *Colores del menú*: Modifica las propiedades de color en create_sidemenu para personalizar los botones del menú lateral.
  
## Ejecución de la Aplicación

Ejecuta el siguiente comando desde la terminal para iniciar la aplicación:

```bash
python main.py
```

## Créditos

Desarrollado con Tkinter, markdown, y tkhtmlview para facilitar la ejecución de scripts y la visualización de documentación desde una interfaz amigable.
