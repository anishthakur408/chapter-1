#Label the program written in problem 4 with comments. 

# importing os 
import os


# for printing directory u want

def print_directory_contents(directory):
    for item in os.listdir(directory):
        print(item)

#which u want path of your directory
directory_path = '/'  

# for printing which doirectory u want

print(f"Contents of directory '{directory_path}':")
print_directory_contents(directory_path)

