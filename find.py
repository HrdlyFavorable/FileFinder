#!/usr/bin/python3
import os
import sys
try:
    if len(sys.argv) != 2:
        print("./oswalk.py + argument expected.")
        print("-h or --help as argument for help menu.")
        sys.exit(0)
    if sys.argv[1] == "-f" or sys.argv[1] == '--file':
        found_files = []
        print("-" * 70)
        print("This application will find a file in a specified working directory.")
        print("-" * 70)
        working_dir = input("Type in a working directory to search: ")
        if working_dir[1] == "~":
            e = working_dir[0] + "home" + working_dir[2:]
            del working_dir
            working_dir = e
        try:
            os.chdir(working_dir)
        except FileNotFoundError:
            print("Not a valid working directory.")
            print('''Example of working dir:
    /home/name/Downloads/
    if you don't know what dir to scan, type in
    /home/ for the directory on linux.''')
            sys.exit(0)
        file = input("Type in the file you want to find: ")
        for dir_path, dir_names, filenames in os.walk(working_dir):
            print(f"scanning directory {dir_path}...")
            for files in filenames:
                if files == file:
                    print(f"File {file} found at {dir_path}")
                    found_files.append(dir_path)

        if not found_files:
            print(f"No file {file} found at working dir {os.getcwd()}")
            sys.exit(0)

        print(f"files with name {file} found at: ")

        for i in found_files:
            print(i)
    elif sys.argv[1] == '-d' or sys.argv[1] == '--directory':
        found_directories = []
        print('-' * 70)
        print("This application will find a directory in a specified working directory.")
        print("-" * 70)
        working_dir = input("Type in a working directory to search: ")
        if working_dir[1] == "~":
            e = working_dir[0] + "home" + working_dir[2:]
            del working_dir
            working_dir = e
        try:
            os.chdir(working_dir)
        except FileNotFoundError:
            print("Not a valid working directory.")
            print('''Example of working dir:
                     /home/name/Downloads/
                     if you don't know what dir to scan type in
                     /home/ for the directory on linux.''')
            sys.exit(0)
        directory = input("Type in the directory you want to find: ")
        for dir_path, dir_names, filenames in os.walk(working_dir):
            print(f"scanning directory {dir_path}...")
            for directories in dir_names:
                if directory == directories:
                    print(f"directory {directory} found at {dir_path}")
                    found_directories.append(dir_path)
        if not found_directories:
            print(f"No file {directory} found at working dir {os.getcwd()}")
            sys.exit(0)
        print(f"directories with name {directory} found at: ")

        for i in found_directories:
            print(i)
    elif sys.argv[1] == "-h" or sys.argv[1] == '--help':
        print('''list of commands:
        1. -f or --file to find a file
        2. -d or --directory to find a directory 
        3. -h or --help for this menu''')
        sys.exit(0)
    else:
        print("invalid argument. -h or --help for help menu.")
        sys.exit(0)
except KeyboardInterrupt:
    print("/n")
    sys.stderr.write("ABORTING PROGRAM...")
    sys.exit(0)
