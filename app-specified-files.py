# Specify filenames to be read
specified_files = ['fileOne.txt', 'fileTwo.txt']

import os
import pyperclip

def copy_files_to_clipboard():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    contents = []

    for filename in specified_files:
        file_path = os.path.join(current_directory, filename)
        
        # Skip if file does not exist
        if not os.path.isfile(file_path):
            print(f'File {filename} not found in the directory. Skipping...')
            continue

        with open(file_path, 'r') as file:
            contents.append(f"{filename}:\n\n{file.read()}\n\n----------\n")

    pyperclip.copy(''.join(contents))

copy_files_to_clipboard()
