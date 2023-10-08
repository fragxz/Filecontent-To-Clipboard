# Filecontent-to-Clipboard
Filecontent-to-Clipboard is a handy Python script designed to streamline your programming workflow by automatically copying the content of all files OR specified files of the current directory to your clipboard.

I use it to quickly copy the content of specific files for ChatGPT prompting.

## How to use
**app.py**

Create a folder, copy your files into it and execute this python script => Now you have the contents of the files in your clipboard

**app-specified-files.py**

Change the specified files inside the code to meet your needs. 
Now you can copy this file into your project and just execute the script whenever you need it!

The content of the clipboard will have the following structure:

```
file1:

CONTENT_OF_FILE1

---------

file2:

CONTENT_OF_FILE2

---------
```

**Remember, the script does not differentiate between file types** and will attempt to read all file types. Large or binary files may cause the script to fail or produce undesired results. It's best used in directories with text-based files like .txt, .csv, .xml, .html, .css, .js, .py, .php, etc.

## How it works

Here's a breakdown of the script's workflow:

* It first identifies the directory where it's currently located using Python's os module.
* Next, it loops over all the files in the said directory.
* It ignores itself (the script file) to prevent unnecessary content copying.
* For each of the other files, it opens the file and reads the content.
* Then, it builds a formatted string with the filename and its content, separated by line breaks for clarity. It also adds a line of hyphens for better visual separation between different files.
* Once it has looped through all the files and collected their contents, it copies the compiled string into your system's clipboard using the pyperclip module.

This script allows you to quickly and efficiently copy an entire directory's file contents into your clipboard, formatted and ready to paste wherever required.

## Requirements

Ensure to have pyperclip Python module installed. If not, install it using pip:

```pip install pyperclip```

Move the script to the directory you want to copy files from and run:

```python3 app.py```
OR
```python3 app-specified-files.py```

**Tip:** You can also change python files to be executed by Python.exe (Windows), so you can execute it with a double-click.

After successful execution, the script's output (contents of the files) is stored in the clipboard, ready for you to paste wherever you like. This script handles all text-based file types present in the directory.
