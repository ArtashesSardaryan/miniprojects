'''
About Programm : A program that will separate the files based on the types(docs, pdf, jpg, etc). The
source directory should be passed as an argument.
Version : 1.0
Author : Artash
'''
import os
import shutil
import sys

def separate_files(source_dir):
    '''Function To separate'''
    # Create directories for each file type
    file_types = set()
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_type = filename.split('.')[-1].lower()
            file_types.add(file_type)
    
    for file_type in file_types:
        os.makedirs(os.path.join(source_dir, file_type), exist_ok=True)
    
    # Move files to their respective directories
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_type = filename.split('.')[-1].lower()
            destination_dir = os.path.join(source_dir, file_type)
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_dir, filename))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python separate_files.py <source_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    if not os.path.isdir(source_directory):
        print("Error: The specified source directory does not exist.")
        sys.exit(1)

    separate_files(source_directory)
    print("Files separated successfully.")
