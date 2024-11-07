import os
import re
import time

from unidecode import unidecode
from datetime import timedelta


print("Ejecutando script...")
start_time = time.time()


def clean_name(name, remove_accent_marks=False, remove_special_characters=False) -> str:
    """
    The function `clean_name` takes a name as input and returns a cleaned version of the name with
    options to remove accent marks and special characters.
    
    :param name: The `clean_name` function takes a `name` as input and has two optional parameters:
    `remove_accent_marks` and `remove_special_characters`. The function replaces spaces in the name with
    underscores and then applies additional cleaning based on the optional parameters
    :param remove_accent_marks: The `remove_accent_marks` parameter in the `clean_name` function
    determines whether accent marks should be removed from the input `name` string. If set to `True`,
    the function will use the `unidecode` function to remove accent marks from the string. If set to
    `False, defaults to False (optional)
    :param remove_special_characters: The `remove_special_characters` parameter in the `clean_name`
    function determines whether special characters should be removed from the input `name` string. If
    set to `True`, the function will use a regular expression to remove any characters that are not
    letters (a-z, A-Z), numbers (0, defaults to False (optional)
    :return: The function `clean_name` returns a cleaned version of the input `name` string based on the
    specified cleaning options. The cleaned name is returned as a string.
    """
    name = name.replace(' ', '_')

    if remove_accent_marks:
        name = unidecode(name)

    if remove_special_characters:
        name = re.sub(r'[^a-zA-Z0-9_\.]', '', name)

    return name


def rename_files_and_folders(root, remove_accent_marks=False, remove_special_characters=False):
    """
    The function `rename_files_and_folders` renames files, folders, and the root directory by cleaning
    their names based on specified options.
    
    :param root: The `root` parameter in the `rename_files_and_folders` function represents the starting
    directory from which you want to rename files and folders. This function will recursively walk
    through all subdirectories and files starting from this root directory
    :param remove_accent_marks: The `remove_accent_marks` parameter in the `rename_files_and_folders`
    function determines whether accent marks should be removed from file and folder names during the
    renaming process. If set to `True`, any accent marks in the names will be removed. If set to
    `False`, the accent marks will, defaults to False (optional)
    :param remove_special_characters: The `remove_special_characters` parameter in the
    `rename_files_and_folders` function determines whether special characters should be removed from the
    names of files and folders during the renaming process. If set to `True`, any special characters
    present in the names will be removed. If set to `False`, the special, defaults to False (optional)
    """
    for current_folder, sub_folders, files in os.walk(root, topdown=False):
        for file in files:
            complete_path = os.path.join(current_folder, file)
            new_name = clean_name(file, remove_accent_marks, remove_special_characters)
            new_complete_path = os.path.join(current_folder, new_name)
            os.rename(complete_path, new_complete_path)

        for folder in sub_folders:
            complete_path = os.path.join(current_folder, folder)
            new_name = clean_name(folder, remove_accent_marks, remove_special_characters)
            new_complete_path = os.path.join(current_folder, new_name)
            os.rename(complete_path, new_complete_path)

        # new_current_folder = clean_name(current_folder, remove_accent_marks, remove_special_characters)
        # if new_current_folder != current_folder:
            # os.rename(current_folder, new_current_folder)


if __name__ == '__main__':
    root = input("Ingrese la ubicación de la carpeta a analizar: ")

    remove_accent_marks = True
    remove_special_characters = True

    rename_files_and_folders(root, remove_accent_marks, remove_special_characters)


    end_time = time.time()
    execution_time = timedelta(seconds=end_time - start_time)

    print(f"Tiempo de ejecución: {execution_time} (hh:mm:ss)")