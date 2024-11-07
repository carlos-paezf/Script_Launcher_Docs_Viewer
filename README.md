# Script Launcher - Docs Viewer

## Descripción

Este proyecto implementa una interfaz gráfica en Python, utilizando la biblioteca `tkinter`, para ejecutar scripts y mostrar documentación asociada. La aplicación permite al usuario seleccionar y ejecutar scripts de Python (`.py`) y ejecutables (`.exe`), además de visualizar archivos README.md en HTML dentro de la interfaz.

## Funcionalidades

1. **Ejecución de Scripts**: Ejecuta scripts `.py` y `.exe` seleccionados por el usuario.
2. **Visualización de README.md**: Muestra el contenido del archivo README.md asociado al script seleccionado en formato HTML.
3. **Almacenamiento en Caché**: Almacena en caché el contenido HTML del README.md de nivel 0 para mejorar la eficiencia en su visualización.
4. **Interfaz con Navegación en Sidemenu**: Incluye un menú lateral que permite seleccionar scripts para ejecutar y ver documentación.
5. **Redirección a GitHub**: Incluye un botón en el menú lateral para redirigir al usuario a un perfil de GitHub.

## Requisitos

- Python 3.x
- Librerías requeridas:
  - `tkinter`: Incluida en la instalación estándar de Python.
  - `tkhtmlview`: Para renderizar el contenido HTML en el GUI.
  - `markdown`: Para convertir el contenido de archivos README.md en HTML.

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

## Uso

Para utilizar el script, sigue estos pasos:

1. Clona el repositorio (opcional):

    ```bash
    git clone <https://github.com/carlos-paezf/Script_Launcher_Docs_Viewer.git>
    ```

2. Organización de scripts: Coloca los scripts `.py` o `.exe` en subdirectorios dentro de la ruta especificada en el código (`C:\\Users\\carlo\\Documents\\Python Scripts` en este ejemplo).
3. Iniciar la Aplicación: Ejecuta el archivo principal de la aplicación.

   ```bash
   python main.py
   ```

4. Seleccionar Script: Usa el menú lateral para elegir un script.
5. Ver README.md: El README.md asociado al script seleccionado (si existe) se mostrará en la ventana principal.
6. Ejecutar Script: Presiona el botón "Ejecutar Script" para ejecutar el script seleccionado.
7. Redirigir a GitHub: Haz clic en el botón "Ir a GitHub - carlos-paezf" para abrir el perfil de GitHub en el navegador.

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
  
## Mejoras Posibles

- Soporte para Más Tipos de Archivos: Extender la funcionalidad para ejecutar otros tipos de archivos y scripts.
- Profundidad de Búsqueda Configurable: Permitir al usuario definir la profundidad de búsqueda en el menú lateral.
- Historial de Ejecución: Implementar un historial de scripts ejecutados recientemente.
- Soporte Multilenguaje: Permitir seleccionar el idioma de la interfaz.

## Descripción de los Métodos en el Código

### Clase `ScriptHandler`

- `__init__`: Inicializa las variables selected_script y readme_cache. Carga en caché el README.md del nivel raíz.
- `cache_root_readme`: Almacena en caché el contenido HTML del archivo README.md en el directorio raíz, si existe.
- `show_root_readme`: Muestra el README.md de nivel raíz en la etiqueta HTML del GUI o un mensaje de error si no se encuentra.
- `run_script`: Ejecuta un script .py o .exe y muestra mensajes de error en el GUI en caso de fallos.
- `find_scripts`: Busca scripts .py y .exe en un directorio y devuelve una lista de sus rutas dentro de una profundidad de 1 a 2 niveles.
- `show_readme`: Muestra el README.md asociado a un script en la etiqueta HTML o un mensaje si el archivo no está presente.
- `get_readme_html`: Convierte el contenido de un archivo README.md en HTML y lo almacena en caché.

### Clase `ViewHandler`

- `__init__`: Configura la ventana principal, define el título, el tamaño, y organiza los componentes en un Grid.
- `create_widgets`: Inicializa los Frames de la interfaz y llama a `create_sidemenu` y `show_content`.
- `on_select`: Cambia el estilo del botón seleccionado y muestra el README.md correspondiente en la etiqueta HTML.
- `create_sidemenu`: Crea botones en el menú lateral para cada script encontrado, junto con los botones para mostrar el README de nivel 0 y redirigir a GitHub.
- `show_content`: Inicializa la etiqueta HTML para mostrar la documentación y agrega un botón para ejecutar el script seleccionado.

## Créditos

Desarrollado con `Tkinter`, `markdown`, y `tkhtmlview` para facilitar la ejecución de scripts y la visualización de documentación desde una interfaz amigable.
