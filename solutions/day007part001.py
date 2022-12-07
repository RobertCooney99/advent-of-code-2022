# ADVENT OF CODE 2022: DAY 007 PART 001
# 
# puzzle input: input is a text file showing
# terminal commands and the outputs. these outputs
# show directories with children directories and 
# files with sizes.
#
# puzzle output: the sum of directory sizes of
# directories with a size <= 100,000.

from utils import aochelper

input = aochelper.text_to_string("7") + "\n"
commands_with_output = input.split("$")

class FileManager:
    def __init__(self):
        self.directories = {}

    def add_directory(self, directory):
        self.directories[directory.name] = directory

    def get_directory_total_deep_size(self, directory_name):
        directory = self.directories[directory_name]
        total_deep_size =  directory.total_shallow_size
        for child_directory in directory.children_directories:
            child_directory_name = f"{directory.name}{child_directory}/"
            total_deep_size += self.get_directory_total_deep_size(child_directory_name)
        return total_deep_size

class Dir:
    def __init__(self, name, children_directories, files):
        self.name = name
        self.children_directories = children_directories
        self.files = files
        self.calc_total_shallow_size()
    
    def calc_total_shallow_size(self):
        sum = 0
        for file in self.files:
            sum += int(file.size)
        self.total_shallow_size = sum

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def directory_reset():
    return "/"

def directory_step_back(current_directory):
    string = ""
    for dir in current_directory.split("/")[:-2]:
        string += f"{dir}/"
    return string

def directory_step_into(current_directory, step_into):
    current_directory += f"{step_into}/"
    return current_directory

directories_from_input = []
current_directory = ""

for command_with_output in commands_with_output[1:]:
    command, *output_lines = command_with_output.split("\n")[:-1]

    command_sections = command.strip().split(" ")
    if command_sections[0] == "ls":
        directories_from_input.append([current_directory, output_lines])
    elif command_sections[0] == "cd":
        _, directory = command_sections
        if directory == "/":
            current_directory = directory_reset()
        elif directory == "..":
            current_directory = directory_step_back(current_directory)
        else:
            current_directory = directory_step_into(current_directory, directory)

file_manager = FileManager()

for directory in directories_from_input:
    files = []
    children_directories = []
    for child in directory[1]:
        child = child.split(" ")
        if child[0] == "dir":
            child_directory_name = child[1]
            children_directories.append(child_directory_name)
        else:
            file_size, file_name = child
            files.append(File(file_name, file_size))
    file_manager.add_directory(Dir(directory[0], children_directories, files))

total_size = 0
for directory in file_manager.directories.values():
    dir_size = file_manager.get_directory_total_deep_size(directory.name)
    if dir_size <= 100000:
        total_size += dir_size

print(f"Total size of directories with size of at most 100000: {total_size}")

