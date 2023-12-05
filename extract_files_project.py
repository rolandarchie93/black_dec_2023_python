#!/usr/bin/env python3.7

import os

# Get the current working directory
current_working_directory = os.getcwd()

# Create an empty list to store file information
file_info = []

# Go through the directory tree and get the file information
for dirpath, dirnames, filenames, in os.walk(current_working_directory):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        file_size = os.path.getsize(file_path)
        file_info.append({"name": file, "size": file_size})

# Print the file information
for file in file_info:
    print(file)