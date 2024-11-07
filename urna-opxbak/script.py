import os
import re
import shutil
import time

from datetime import timedelta


print("Ejecutando script...")
start_time = time.time()


origin_folder = os.getcwd()
destination_folder = os.path.join(origin_folder, "OPXBAK")
destination_completed_folder = os.path.join(origin_folder, "Completed")


after_batch_pattern = re.compile(r".*ab.*", re.IGNORECASE)


def move_file(file, source_path, before_batch_destination_folder, after_batch_destination_folder):
    """
    Moves a file to either a before-batch or after-batch destination folder based on a pattern match.

    :param file: The name of the file to be moved.
    :param source_path: The source path of the file.
    :param before_batch_destination_folder: The destination folder for files that don't match the pattern.
    :param after_batch_destination_folder: The destination folder for files that match the pattern.
    """
    with open("log.txt", 'a') as log_file:
        if after_batch_pattern.match(file):
            shutil.move(source_path, after_batch_destination_folder)
            log_file.write(f"file: {file}\n")
            log_file.write(f"source_path: {source_path}\n" )
            log_file.write(f"after_batch_destination_folder: {after_batch_destination_folder}\n\n")
        else:
            shutil.move(source_path, before_batch_destination_folder)
            log_file.write(f"file: {file}\n")
            log_file.write(f"source_path: {source_path}\n" )
            log_file.write(f"before_batch_destination_folder: {before_batch_destination_folder}\n\n")


def validate_duplicated(file, origin, before_batch_destination_folder):
    """
    Validates if a file with the same name already exists in the before-batch destination folder,
    and renames the file if necessary to avoid duplication.

    :param file: The name of the file to be validated.
    :param origin: The source directory containing the file.
    :param before_batch_destination_folder: The destination folder for files before batch processing.

    :return: The new source path of the file after potential renaming.
    """
    source_path = os.path.join(origin, file)
    new_source_path = source_path

    before_batch_file = os.path.join(before_batch_destination_folder, file)

    if os.path.exists(before_batch_file):
        current_file_modification_time = os.path.getmtime(source_path)
        existing_file_modification_time = os.path.getmtime(before_batch_file)

        if (current_file_modification_time > existing_file_modification_time):
            name_split = file.split('.')

            if not after_batch_pattern.match(name_split[0]):
                new_file_name = name_split[0] + 'ab.' + name_split[1]
                new_source_path = os.path.join(origin, new_file_name)
                os.rename(source_path, new_source_path)            

    else:
        new_source_path = source_path

    return new_source_path


def relocate_files(origin, before_batch_destination_folder, after_batch_destination_folder):
    """
    Recursively relocates files from the origin directory to either the before-batch or after-batch destination folder.

    :param origin: The source directory containing the files to be relocated.
    :param before_batch_destination_folder: The destination folder for files before batch processing.
    :param after_batch_destination_folder: The destination folder for files after batch processing.
    """
    for file in os.listdir(origin):
        source_path = os.path.join(origin, file)
        if os.path.exists(source_path) and os.path.isfile(source_path):
            source_path = validate_duplicated(file, origin, before_batch_destination_folder)
            move_file(file, source_path, before_batch_destination_folder, after_batch_destination_folder)
        else:
            relocate_files(source_path, before_batch_destination_folder, after_batch_destination_folder)


for subfolder in os.listdir(origin_folder):
    subfolder_path = os.path.join(origin_folder, subfolder)

    if subfolder in("OPXBAK", "Completed", "script.py"):
        continue

    if os.path.isdir(subfolder_path):
        before_batch_destination_folder = os.path.join(destination_folder, subfolder[:-3])
        after_batch_destination_folder = os.path.join(destination_folder, subfolder[:-3] + "AB")

        if not os.path.exists(before_batch_destination_folder):
            os.makedirs(before_batch_destination_folder)

        if not os.path.exists(after_batch_destination_folder):
            os.makedirs(after_batch_destination_folder)

        relocate_files(subfolder_path, before_batch_destination_folder, after_batch_destination_folder)

        shutil.move(subfolder, destination_completed_folder)


end_time = time.time()
execution_time = timedelta(seconds=end_time - start_time)


print(f"Tiempo de ejecución: {execution_time} (hh:mm:ss)")