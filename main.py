import markdown
import os
import subprocess  
import tkinter as tk

from tkhtmlview import HTMLLabel


class App(tk.Tk):
    def __init__(self):
        """
        The function initializes a GUI window with a side menu and content frame for executing scripts
        and displaying documentation.
        """
        super().__init__()

        self.title("Ejecutar Scripts y Documentación")
        self.geometry("1200x900")

        self.columnconfigure(0, weight=0)
        self.rowconfigure(0, weight=1)

        self.sidemenu_frame = tk.Frame(self, bg="#2c3e50", width=300)
        self.sidemenu_frame.grid(row=0, column=0, sticky="nsw")

        self.content_frame = tk.Frame(self)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=50, pady=20)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.selected_script = tk.StringVar()

        self.create_sidemenu()
        self.show_content()


    def run_script(self, script_path: str):
        """
        The function `run_script` executes a Python script if the file path ends with '.py', an
        executable file if it ends with '.exe', or displays a message if neither condition is met.
        
        :param script_path: The `script_path` parameter is a string that represents the file path of the
        script that you want to run. The function `run_script` checks the file extension of the script
        path and runs the script accordingly using `subprocess.run`. If the file extension is '.py', it
        runs the script
        :type script_path: str
        """
        if script_path.endswith('py'):
            subprocess.run(['python', script_path])
        elif script_path.endswith('exe'):
            subprocess.run([script_path])
        else:
            self.html_label.set_html("<h1>Por favor, selecciona un script para realizar la ejecución</h1>")


    def find_scripts(self, directory: str):
        """
        The function `find_scripts` takes a directory path as input and returns a list of Python (.py)
        and executable (.exe) script files found within that directory and its subdirectories.
        
        :param directory: The `directory` parameter in the `find_scripts` method is a string that
        represents the path to the directory where you want to search for scripts. This method searches
        for Python scripts (files with a `.py` extension) and executable scripts (files with a `.exe`
        extension) within the specified
        :type directory: str
        :return: The function `find_scripts` returns a list of file paths for all Python (.py) and
        executable (.exe) scripts found within the specified directory and its subdirectories.
        """
        scripts = []

        for root, _, files in os.walk(directory):
            if root != directory:
                for file in files:
                    if file.endswith('.py') or file.endswith('.exe'):
                        scripts.append(os.path.join(root, file))

        return scripts


    def show_readme(self, script_path):
        """
        The function `show_readme` reads a README.md file, converts its content to HTML using the markdown
        library, and displays it in an HTML label if the file exists; otherwise, it displays a message
        indicating that the README.md file was not found.
        
        :param html_label: The `html_label` parameter is likely an object that represents a label or element
        in a graphical user interface (GUI) that can display HTML content. In the `show_readme` function,
        this parameter is used to set the HTML content of the label based on the contents of a README.md
        file
        :param script_path: The `script_path` parameter in the `show_readme` function is the path to the
        script file for which you want to display the README.md content. This parameter is used to locate
        the README.md file in the same directory as the script file
        """
        readme_path = os.path.join(os.path.dirname(script_path), 'README.md')
        
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding="utf-8") as file:
                markdown_text = file.read()
                html_text = markdown.markdown(markdown_text)
                self.html_label.set_html(html_text)
        else:
            self.html_label.set_html("<h1>No README.md found</h1>")


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
        for btn in self.sidemenu_frame.winfo_children():
            btn.config(bg="#34495e", fg="white")

        button.config(bg="white", fg="black")

        self.show_readme(script)
    

    def create_sidemenu(self):
        """
        The function `create_sidemenu` creates radio buttons in a tkinter side menu based on scripts
        found in a directory.
        """
        scripts = self.find_scripts('C:\\Users\\carlo\\Documents\\Python Scripts')

        for script in scripts:
            folder_name = os.path.basename(os.path.dirname(script)).split('/')[-1]

            button = tk.Radiobutton(
                self.sidemenu_frame, 
                text=folder_name,
                variable=self.selected_script,
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

    
    def show_content(self):
        """
        The `show_content` function displays HTML content from a README.md file and includes a button to
        execute a selected script.
        """
        self.html_label = HTMLLabel(self.content_frame, html="<h1>Selecciona un script para ver la documentación</h1>")
        self.html_label.pack(fill="both", expand=True)

        with open('./README.md', 'r', encoding="utf-8") as file:
            markdown_text = file.read()
            html_text = markdown.markdown(markdown_text)
            self.html_label.set_html(html_text)

        execute_button = tk.Button(
            self.content_frame, 
            text="Ejecutar Script", 
            command=lambda: self.run_script(self.selected_script.get()),
            font=("Arial", 12),
            anchor="w",
            padx=50,
            bg="#34495e",
            fg="white"
        )
        execute_button.pack(pady=20)



if __name__ == '__main__':
    app = App()
    app.mainloop()