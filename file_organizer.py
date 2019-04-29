#  Source code of the file organizer
#  file_organizer.py by Sudipto Roy
#  Run this python file in any folder or directory to organize the files

__author__ = 'Sudipto Roy'
__copyright__ = 'Copyright 2019, File organizer project'
__maintainter__ = 'Sudipto Roy'
__email__ = 'sudiptoroy.cse@gmail.com'

from os import listdir, mkdir, rename, path
from os.path import isfile, join, exists

source_folder = path.abspath(path.curdir)   # fetching the absulate path of current directory
list_item = listdir(source_folder)   # List of the files
extension_to_folder_mapper = {       # Categorizing with file extension
    'jpg jpeg gif png svg' : 'images',
    'app dmg pkg exe' : 'applications',
    'apk' : 'android apps',
    'txt xlxs xls doc docx pdf' : 'documents',
    'zip tar gz bz2 rar 7zip' : 'compressed files',
    'py pyc c cpp cs sh whl r js html css php ts' : 'programming files',
    'mp3 amr wav m4a m4b m4p webm' : 'audio files'

}

def create_folder(name):  # function to create folder
    if not exists(join(source_folder, name)):
        mkdir(join(source_folder, name))

def move_file_to_folder(file_name,folder_name):  # function to move the files to new folder
    old_path = join(source_folder, file_name)
    new_path = join(source_folder, folder_name, file_name)
    rename(old_path, new_path)

def map_extension_to_folder (extension, name):  # detect the extension of the files and organize the files
    folder_name = 'others'
    for extension_list, destination_folder in extension_to_folder_mapper.items():  # Checking the file extension with the dictionary
        if extension in extension_list.split(' '):  
            folder_name = destination_folder
            break
    
    create_folder(folder_name)  # Creating new folder
    move_file_to_folder(name, folder_name)  # Moving files to the folders

def get_file_extension(file_name):  # function for getting file extension
    split_name = file_name.split('.')  # split the file name
    return split_name[-1]  # return the extension

def main():
    for item_name in list_item:
        if isfile(join(source_folder, item_name)):  # Checking for valid file
            file_extension = get_file_extension(item_name)  # get file extension
            map_extension_to_folder(file_extension, item_name)  # map the extension for organizing

main()