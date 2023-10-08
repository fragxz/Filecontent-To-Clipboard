import os
import pyperclip

def copy_files_to_clipboard():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    contents = []
    
    for filename in os.listdir(current_directory):
        if filename == os.path.basename(__file__):
            continue  # Skip the script itself
            
        with open(os.path.join(current_directory, filename), 'r') as file:
            contents.append(f"{filename}:\n\n{file.read()}\n\n----------\n")

    pyperclip.copy(''.join(contents))

copy_files_to_clipboard()
