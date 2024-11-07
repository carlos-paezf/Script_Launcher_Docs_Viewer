import os
import time
import re
import pandas as pd
 
from datetime import datetime, timedelta
from pathlib import Path
from datetime import datetime
 
 
print("Ejecutando script...")
start_time = time.time()
 
 
def is_valid_name(name: str) -> bool:
    """
    The function `is_valid_name` checks if a given string only contains alphanumeric characters and
    underscores.
   
    :param name: The `is_valid_name` function takes a string input `name` and checks if it consists of
    only alphanumeric characters and underscores. It returns `True` if the name is valid according to
    this pattern, and `False` otherwise
    :type name: str
    :return: The function `is_valid_name` is returning a boolean value, either `True` or `False`, based
    on whether the input `name` is a valid name according to the specified pattern.
    """
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    return pattern.match(name) is not None
 
 
def check_keywords(string: str, keywords: set) -> bool:
    """
    The function `check_keywords` takes a string and a set of keywords, converts the string to
    lowercase, and returns True if any of the keywords are found in the lowercase string.
   
    :param string: A string of text that you want to check for the presence of certain keywords
    :type string: str
    :param keywords: The `keywords` parameter is a set containing the keywords that we want to check for
    in the given `string`
    :type keywords: set
    :return: The function `check_keywords` returns a boolean value, indicating whether any of the
    keywords in the given set are present in the lowercase version of the input string.
    """
    string_lower = string.lower()
    return any(keyword in string_lower for keyword in keywords)
 
 
def check_keywords_in_path_and_file(path: str, file: str, keywords: set) -> bool:
    """
    This function checks if any keyword in a set is present in either the lowercase path or file name.
   
    :param path: The `path` parameter is a string representing the path to a directory or file
    :type path: str
    :param file: The `file` parameter in the `check_keywords_in_path_and_file` function represents the
    name of a file. It is a string that contains the name of the file (including the file extension)
    :type file: str
    :param keywords: A set of keywords that you want to check for in the path and file names
    :type keywords: set
    :return: a boolean value indicating whether any keyword in the given set is found in the lowercase
    version of the path or the lowercase version of the file name.
    """
    path_lower = path.lower()
    file_lower = file.lower()
    return any(keyword in path_lower or keyword in file_lower for keyword in keywords)
 
 
def file_has_allowed_extension(file: str, allowed_extensions: set) -> bool:
    """
    The function checks if a file has an allowed extension based on a set of allowed extensions.
   
    :param file: The `file` parameter is a string that represents the name of a file
    :type file: str
    :param allowed_extensions: The `allowed_extensions` parameter is a set containing the file
    extensions that are considered allowed. For example, if you want to allow files with extensions
    ".txt", ".csv", and ".pdf", you would create a set like this: `{"txt", "csv", "pdf"}`. The
    :type allowed_extensions: set
    :return: The function `file_has_allowed_extension` is returning a boolean value indicating whether
    the given `file` has an extension that is included in the `allowed_extensions` set.
    """
    return any(file.endswith(extension) for extension in allowed_extensions)
 
 
def get_metadata(current_folder: str, file: str, path: str):
    """
    The function `get_metadata` retrieves various metadata information about a file in a specified
    folder.
   
    :param current_folder: The `current_folder` parameter represents the current directory where the
    file is located
    :type current_folder: str
    :param file: The `get_metadata` function takes several parameters to gather metadata information
    about a file. The `file` parameter represents the name of the file for which you want to retrieve
    metadata
    :type file: str
    :param path: The `get_metadata` function takes several parameters to gather metadata information
    about a file within a specified folder. Here's a breakdown of the parameters:
    :type path: str
    :return: The function `get_metadata` is returning a tuple containing various metadata information
    about a file located in a specific folder. The elements of the tuple are as follows:
    """
    file_path = os.path.join(current_folder, file)
    file_size = os.path.getsize(file_path)
    modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))
    levels = len(os.path.relpath(current_folder, path).split(os.sep))
    name_len = len(Path(file).stem)
 
    audit_relate = check_keywords_in_path_and_file(current_folder, file, {"auditoria"})
    opics_relate = check_keywords_in_path_and_file(current_folder, file, {"opics"})
    sigo_relate = check_keywords_in_path_and_file(current_folder, file, {"sigo"})
    contingency_relate = check_keywords_in_path_and_file(current_folder, file, {"contingency", "contingencia"})
    training_relate = check_keywords_in_path_and_file(current_folder, file, {"capacitacion", "capacitación"})
 
    is_pdf = ".pdf" in file
    is_office_file = check_keywords(file, {".doc", ".docx", ".dotx", ".csv", ".xls", ".xlsx", ".pptx"})
    is_manual = check_keywords_in_path_and_file(current_folder, file, {"manual"})
    is_log = (
            "log" in file.lower()
        and not "logi" in file.lower()
        and not ".doc" in file.lower()
        and not "dialog" in file.lower()
    )
    is_backup = check_keywords(file, {"backup"})
    is_instructive = check_keywords(file, {"ins_", "instructivo", "instructive"})
    is_video = check_keywords(file, {".mp4", ".mov", ".avi", ".mkv"})
    is_part_of_a_develop = check_keywords(file, {".pl", ".pm", ".py", ".java", ".class", ".ts", ".js", ".html", ".css", ".cs", ".csproj", ".vb", ".ipynb"})
    is_pst = ".pst" in file.lower()
 
    valid_file_name = is_valid_name(file)
 
    return (
            current_folder, file, file_size, modification_time, levels, name_len,
        audit_relate, opics_relate, sigo_relate, contingency_relate, training_relate,
        is_pdf, is_office_file, is_manual, is_log, is_backup, is_instructive,
        is_video, is_part_of_a_develop, is_pst,
        valid_file_name
    )
 
 
def get_files_info(path: str, allowed_extensions: set = None):
    """
    The function `get_files_info` retrieves metadata for files in a specified path, filtering by allowed
    extensions if provided.
   
    :param path: The `path` parameter in the `get_files_info` function is a string that represents the
    directory path from which you want to retrieve file information
    :type path: str
    :param allowed_extensions: The `allowed_extensions` parameter is a set that contains the file
    extensions that are allowed to be included in the files information list. If this parameter is not
    provided (i.e., set to `None`), then all files in the specified path will be considered without any
    restriction based on file extensions
    :type allowed_extensions: set
    :return: A list of dictionaries containing metadata information for files in the specified path that
    have allowed extensions, if provided.
    """
    files_info = []
 
    for current_folder, sub_folder, files_in_folder in os.walk(path):
        for file in files_in_folder:
            if allowed_extensions is None or file_has_allowed_extension(file, allowed_extensions):
                metadata = get_metadata(current_folder, file, path)
                files_info.append(metadata)
    return files_info
 
 
def define_io_paths() -> str:
    """
    The function `define_io_paths` takes user input for base directory and destination folder, then
    constructs an Excel file path based on the input.
    :return: The function `define_io_paths()` is returning two values: `base_directory` and
    `excel_file_path`.
    """
    now = datetime.now()
    formatted_date = now.strftime("%d%m%y-%H%M")
   
    base_directory = input("Ingrese la dirección de la carpeta base: ")
    excel_file_path = input("Ingrese la dirección de la carpeta destino: ") + '\\' + base_directory.split("\\")[-1] + '_' + formatted_date + '.xlsx'
 
    return base_directory, excel_file_path
 
 
if __name__ == '__main__':  
    base_directory, excel_file_path = define_io_paths()
    allowed_extensions = None
    files_info = get_files_info(base_directory, allowed_extensions)
   
 
    df = pd.DataFrame(files_info, columns=[
            "Directorio", "Nombre de archivo", "Tamaño (bytes)", "Última fecha de modificación", "Sub-niveles", "Longitud del nombre",
        "Relacionado a Auditoria", "Relacionado a OPICS", "Relacionado a SIGO", "Relacionado a Contingencia", "Relacionado a Capacitación",
        "Es un pdf", "Es un archivo ofimático", "Es un manual", "Es un log", "Es un backup", "Es un instructivo",
        "Es un video", "Es parte de un desarrollo", "Es un pst",
        "Archivo cumple reglas de nombre"
    ])
    df.to_excel(excel_file_path, index=False)
   
    
    end_time = time.time()
    execution_time = timedelta(seconds=end_time - start_time)
   
    print("Listado de archivos guardado en: ", excel_file_path)
    print(f"Tiempo de ejecución: {execution_time} (hh:mm:ss)")