import os
import shutil
import time


def measure_run_time(func):
    """
    The `measure_run_time` function is a Python decorator that measures the execution time of a given
    function.
    
    :param func: The `func` parameter in the `measure_run_time` function is a function that you want to
    measure the execution time of. The `measure_run_time` function is a decorator that calculates the
    time taken for the provided function to execute and prints out the duration in seconds after the
    function has completed its
    :return: The `measure_run_time` function is returning the `wrap` function, which is a wrapper
    function that measures the execution time of the input function `func`.
    """
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'\n\n>>> La función {func.__name__} tardó {end_time - start_time} segundos en ejecución')
        return result
    return wrap


@measure_run_time
def process_files():
    """
    Processes input files and performs the following actions:

    1. Reads input files named in the format 'GRSSYREY.g0X' where X ranges from 1 to 9.
    2. Searches for files in a specific directory that contain keywords extracted from each line of the input files.
    3. Copies the found files to a destination directory.
    4. Writes the corresponding lines to output files named in the format 'GRSSYREY.g0X' in the destination directory.
    5. Prints information about the number of lines read and written in each file.

    Directories and files used:
    - Search directory: 'Z:\\OPXGRSS'
    - Destination directory: 'Z:\\OPXGRSSPROD'
    - Input files: 'Z:\\OPXGRSS\\GRSSYREY.g0X'
    - Output files: 'Z:\\OPXGRSSPROD\\GRSSYREY.g0X'
    """
    for i in range(1, 10):
        input_file = f"Z:\\OPXGRSS\\GRSSYREY.g0{i}"
        output_file = f"Z:\\OPXGRSSPROD\\GRSSYREY.g0{i}"
        search_directory = "Z:\\OPXGRSS"
        destination_directory = "Z:\\OPXGRSSPROD"


        with open(input_file, 'r') as file:
            lines = file.readlines()
            print(f'Leyendo archivo: {input_file}. Cantidad de líneas en el archivo: {len(lines)}')


        with open(output_file, 'w') as out_file:
            for line in lines:
                keyword = line.split(',')[0].lower()

                found_files = [f for f in os.listdir(search_directory) if keyword in f.lower()]

                if found_files:
                    for file_name in found_files:
                        shutil.copy2(os.path.join(search_directory, file_name), destination_directory)

                    out_file.write(line)


        with open(output_file, 'r') as out_file_r:
            out_lines = out_file_r.readlines()
            print(f'\t---> Archivo generado: {output_file}. Cantidad de líneas en el archivo: {len(out_lines)}')


def validate_code():
    """
    The function reads a file, extracts keywords from each line, and searches for files containing those
    keywords in a specified directory.
    """
    input_file = "Z:\\OPXGRSS\\GRSSYREY.g07"
    search_directory = "Z:\\OPXGRSS"

    with open(input_file, 'r') as file:
        lines = file.readlines()
        print(f'Leyendo archivo: {input_file}. Cantidad de líneas en el archivo: {len(lines)}')

    for line in lines:
        keyword = line.split(',')[0].lower()

        found_files = [f for f in os.listdir(search_directory) if keyword in f.lower()]
        print(found_files)


if __name__ == '__main__':
    # process_files()
    validate_code()