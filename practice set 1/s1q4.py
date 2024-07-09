# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.  



import os

def print_directory_contents(directory):
    # List all files and directories in the specified directory
    for item in os.listdir(directory):
        print(item)

# Example usage:
directory_path = '/'  # Replace with your directory path
print(f"Contents of directory '{directory_path}':")
print_directory_contents(directory_path)
