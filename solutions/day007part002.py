# ADVENT OF CODE 2022: DAY 007 PART 002
# 
# puzzle input: input is a text file showing
# terminal commands and the outputs. these outputs
# show directories with children directories and 
# files with sizes. the system has a disk space of
# 70,000,000 but requires at least 30,000,000 to be
# available for an update.
#
# puzzle output: the total size of the smallest
# directory that can be deleted to make space for
# the update.

from utils import aochelper

input = aochelper.text_to_string("7") + "\n"
commands_with_output = input.split("$")

class FileManager:
    def __init__(self):
        self.directories = {}

    def add_directory(self, directory):
        self.directories[directory.name] = directory

    def get_list_of_directory_sizes(self):
        directory_size_map = []
        for directory in self.directories.values():
            directory_size_map.append([directory.name, directory.total_deep_size])
        return directory_size_map

    def get_directory_total_deep_size(self, directory_name):
        directory = self.directories[directory_name]
        total_deep_size =  directory.total_shallow_size
        for child_directory in directory.children_directories:
            child_directory_name = f"{directory.name}{child_directory}/"
            total_deep_size += self.get_directory_total_deep_size(child_directory_name)
        directory.total_deep_size = total_deep_size
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

for directory in file_manager.directories.values():
    dir_size = file_manager.get_directory_total_deep_size(directory.name)

total_space_available = 70000000
unused_space_required = 30000000

directory_size_list = file_manager.get_list_of_directory_sizes()
directory_size_list = sorted(file_manager.get_list_of_directory_sizes(), key=lambda x: x[1], reverse=True)

current_space_used = total_space_available - directory_size_list[0][1]
minimum_amount_to_delete = unused_space_required - current_space_used

directory_to_delete = []
for directory in directory_size_list[1:]:
    if int(directory[1]) >= minimum_amount_to_delete:
        directory_to_delete = directory
    else:
        break

print(f"Directory to delete is '{directory_to_delete[0]}' with a total size of: {directory_to_delete[1]}")
