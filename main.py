import markdown
import subprocess
import shutil
import threading
import tkinter as tk
import webbrowser

from pathlib import Path
from tkhtmlview import HTMLLabel


# The `ScriptHandler` class provides methods to run Python or executable scripts, find scripts in
# directories, and display README.md content as HTML.
class ScriptHandler():
    def __init__(self):
        """
        The `__init__` function initializes variables `selected_script` and `readme_cache` in a Python
        class.
        """
        self.selected_script = tk.StringVar()
        self.readme_cache = {}
        self.cache_root_readme()

    
    def cache_root_readme(self):
        """
        This function caches the HTML content of the root README.md file if it exists.
        """
        root_readme_path = Path('./README.md')
        if root_readme_path.exists():
            self.readme_cache[root_readme_path] = self.get_readme_html(root_readme_path)

    
    def show_root_readme(self, html_label):
        """
        This Python function displays the content of a README.md file located in the root directory, or
        a message if the file is not found.
        
        :param html_label: The `html_label` parameter is likely an object or component that is used to
        display HTML content in a graphical user interface. In this context, it seems to be used to
        display the content of a README file in HTML format. The `set_html` method of `html_label` is
        used to
        """
        root_readme_path = Path('./README.md')
        if root_readme_path in self.readme_cache:
            html_label.set_html(self.readme_cache[root_readme_path])
        else:
            html_label.set_html("<h1>No hay README.md en el nivel raíz</h1>")


    def run_script(self, script_path: str, html_label):
        """
        The function `run_script` executes a Python or executable script based on the file extension and
        displays error messages in an HTML label.
        
        :param script_path: The `script_path` parameter is a string that represents the file path of the
        script that you want to run. It can be either a Python script (ending with '.py') or an
        executable file (ending with '.exe')
        :type script_path: str
        :param html_label: The `html_label` parameter seems to be an object that allows you to set HTML
        content. In the provided code snippet, it is used to display messages or errors related to the
        execution of scripts. When an error occurs during the execution of a script, the `html_label` is
        updated with an
        """
        def script_execution():
            try:
                if script_path.endswith('py'):
                    subprocess.run(['python', script_path], check=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
                elif script_path.endswith('exe'):
                    subprocess.run([script_path], check=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    html_label.set_html("<h1>Por favor, selecciona un script para realizar la ejecución</h1>")
            except subprocess.CalledProcessError as exception:
                html_label.set_html(
                    f'''
                    <h1>Error al ejecutar el script:</h1>
                    <pre>{exception}</pre>
                    <p>Consulta la consola para más información</p>
                    '''
                )
        
        script_thread = threading.Thread(target=script_execution, daemon=True)
        script_thread.start()
        

    def find_scripts(self, directory: str):
        """
        The function `find_scripts` takes a directory path as input and returns a list of paths to
        Python (.py) and executable (.exe) scripts within a specified depth range.
        
        :param directory: The `find_scripts` method takes a `directory` parameter, which is a string
        representing the path to the directory where you want to search for scripts. The method will
        search for scripts with the extensions '.py' and '.exe' within the specified directory and its
        subdirectories within a certain depth range
        :type directory: str
        :return: A list of file paths for all Python (.py) and executable (.exe) scripts found within
        the specified directory and its subdirectories, with a minimum depth of 1 and a maximum depth of
        2 from the specified directory.
        """
        directory_path = Path(directory)
        min_depth = 1
        max_depth = 2

        scripts = {}

        for path in directory_path.rglob('*'):
            if min_depth < len(path.relative_to(directory_path).parts) <= max_depth:
                if path.suffix  == '.exe':
                    scripts[path.parent] = path
                elif path.suffix == '.py' and path.parent not in scripts:
                    scripts[path.parent] = path

        return [str(path) for path in scripts.values()]


    def show_readme(self, script_path, html_label):
        """
        This Python function reads the content of a README.md file located in the same directory as the
        script and displays it as HTML in a specified label, or shows a message if the README.md file is
        not found.
        
        :param script_path: The `script_path` parameter is the path to the script file for which you
        want to display the README.md content. This function reads the README.md file located in the
        same directory as the script file and displays its content as HTML in the specified
        `html_label`. If the README.md file is not
        :param html_label: The `html_label` parameter is likely an object that represents a label or
        element in a graphical user interface (GUI) that can display HTML content. In the context of the
        `show_readme` method, it seems that `html_label` is being used to display the contents of a
        README.md
        """
        readme_path = Path(script_path).parent / 'README.md'
        
        if readme_path.exists():
            html_label.set_html(self.get_readme_html(readme_path))
        else:
            html_label.set_html("<h1>No README.md found</h1>")

    
    def get_readme_html(self, readme_path):
        """
        The function `get_readme_html` reads a markdown file, converts it to HTML, and caches the result
        for future use.
        
        :param readme_path: The `readme_path` parameter in the `get_readme_html` method is the path to
        the README file that you want to convert to HTML. This method reads the content of the README
        file, converts it from Markdown to HTML using the `markdown` library, and caches the HTML
        content for
        :return: The `get_readme_html` method returns the HTML content of the README file located at the
        specified `readme_path`. If the HTML content for the README file has been previously cached in
        `self.readme_cache`, it will return the cached HTML content directly. Otherwise, it reads the
        markdown content from the README file, converts it to HTML using the `markdown.markdown`
        function, caches the
        """
        if readme_path in self.readme_cache:
            return self.readme_cache[readme_path]
        
        with open(readme_path, 'r', encoding="utf-8") as file:
            markdown_text = file.read()
            html_text = markdown.markdown(markdown_text)
            self.readme_cache[readme_path] = html_text
        return html_text
    

    def generate_executables(self, html_label):
        directory_path = Path('./')
        scripts = [
            path for path in directory_path.rglob("*.py")
            if "venv" not in str(path) and "__pycache__" not in str(path)
        ]

        for script in scripts:
            exe_path = script.with_suffix('.exe')

            if not exe_path.exists():
                try:
                    subprocess.run(
                        ['pyinstaller', '--onefile', '--noconsole', str(script)],
                        check=True, creationflags=subprocess.CREATE_NEW_CONSOLE
                    )
                    dist_path = Path('./dist') / script.stem
                    if dist_path.exists():
                        shutil.move(dist_path, exe_path)
                        html_label.set_html(f"<p>Generado: {exe_path}</p>")
                except subprocess.CalledProcessError as exception:
                    html_label.set_html(
                        f'''
                        <h1>Error al generar el ejecutable para {script}:</h1>
                        <pre>{exception}</pre>
                        <p>Consulta la consola para más información</p>
                        '''
                    )



# The `ViewHandler` class creates a GUI window with a side menu for executing scripts and displaying
# documentation.
class ViewHandler(tk.Tk):
    def __init__(self):
        """
        The function initializes a GUI window with a side menu and content frame for executing scripts
        and displaying documentation.
        """
        super().__init__()

        self.script_handler = ScriptHandler()

        self.title("Ejecutar Scripts y Documentación")
        self.geometry("1200x900")

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.create_widgets()

    
    def create_widgets(self):
        """
        The function creates two frames for a GUI layout and calls two other functions to populate them.
        """
        self.sidemenu_frame = tk.Frame(self, bg="#2c3e50", width=350)
        self.sidemenu_frame.grid(row=0, column=0, sticky="nsw")

        self.content_frame = tk.Frame(self)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=50, pady=20)
        
        self.create_sidemenu()
        self.show_content()


    def on_select(self, button, script):
        """
        The `on_select` function changes the background and foreground colors of buttons in a side menu
        and then displays a readme based on the selected script.
        
        :param button: The `button` parameter in the `on_select` method represents the button widget
        that was selected by the user. This method is typically used in GUI applications to handle
        events when a button is clicked or selected by the user
        :param script: The `script` parameter in the `on_select` method is likely a reference to a
        script or code snippet that is associated with the button being selected. This method is
        responsible for updating the appearance of the buttons in a side menu by changing their
        background and foreground colors, and then displaying the readme or
        """
        if hasattr(self, 'last_selected') and self.last_selected:
            self.last_selected.config(bg="#34495e", fg="white")
            
        button.config(bg="white", fg="black")
        self.last_selected = button
        self.script_handler.show_readme(script, self.html_label)
    

    def create_sidemenu(self):
        """
        The function `create_sidemenu` creates radio buttons in a tkinter side menu based on scripts
        found in a directory.
        """
        scripts = self.script_handler.find_scripts('./')

        for script in scripts:
            folder_name = Path(script).parent.name
            
            button = tk.Radiobutton(
                self.sidemenu_frame, 
                text=folder_name,
                variable=self.script_handler.selected_script,
                value=script,
                indicatoron=0,
                bg="#34495e",
                fg="white",
                bd=0,
                padx=75,
                pady=10,
                font=("Arial", 12),
                anchor="w"
            )
            button.config(command=lambda b=button, s=script: self.on_select(b, s))
            button.pack(fill="x")

        bottom_frame = tk.Frame(self.sidemenu_frame, bg="#2c3e50")
        bottom_frame.pack(side="bottom", fill="x", pady=20)


        readme_button = tk.Button(
            bottom_frame,
            text="Mostrar README Nivel 0",
            command=lambda: self.script_handler.show_root_readme(self.html_label),
            bg="#34495e",
            fg="white",
            font=("Arial", 10)
        )
        readme_button.pack(pady=(0, 5))

        generate_exe_button = tk.Button(
            bottom_frame,
            text="Generar Ejecutables",
            command=lambda: self.script_handler.generate_executables(self.html_label),
            bg="#34495e",
            fg="white",
            font=("Arial", 10)
        )
        generate_exe_button.pack(pady=(0, 5))

        github_button = tk.Button(
            bottom_frame,
            text="Ir a GitHub - carlos-paezf",
            command=lambda: webbrowser.open("https://github.com/carlos-paezf"),
            bg="#34495e",
            fg="white",
            font=("Arial", 10)
        )
        github_button.pack(pady=(0, 5))


    
    def show_content(self):
        """
        The `show_content` function displays HTML content from a README.md file and includes a button to
        execute a selected script.
        """
        self.html_label = HTMLLabel(self.content_frame, html="<h1>Selecciona un script para ver la documentación</h1>")
        self.html_label.pack(fill="both", expand=True)

        readme_path = Path('./README.md')

        if readme_path.exists():
            with readme_path.open('r', encoding="utf-8") as file:
                html_text = markdown.markdown(file.read())

            self.html_label.set_html(html_text)

        execute_button = tk.Button(
            self.content_frame, 
            text="Ejecutar Script", 
            command=lambda: self.script_handler.run_script(self.script_handler.selected_script.get(), self.html_label),
            font=("Arial", 12),
            anchor="w",
            padx=50,
            bg="#34495e",
            fg="white"
        )
        execute_button.pack(pady=20)


if __name__ == '__main__':
    app = ViewHandler()
    app.mainloop()