import os 
from typing import List

'''
Step 1: Basics functionlaity 
'''

# Create a dictionary with our file structure 
file_structure = {
    "src/": {
        "models/": None,
        "routes/": None,
        "services/": None,
        "app.py": None
    },
    ".gitignore": None,
    "dockerfile": None,
    "main.py": None,
    "readme.md": None,
    "requirements.txt": None
}

def create_folder(path: str, folder_name: str):
    '''
    Create the folder structure

    Params: 
        path: The path to the folder
        folder_name: The name of the folder to create 

    Returns:
        None 
    '''

    # Make sure that the folder does not exist already
    if os.path.exists(f"{path}/{folder_name}"):
        return
    
    os.mkdir(f"{path}/{folder_name}")


def create_file(path: str, file_name: str):
    '''
    Create the file structure

    Params: 
        path: The path to the folder
        file_name: The name of the file to create 

    Returns:
        None 
    '''
    with open(f"{path}/{file_name}", "w") as file:
        file.write("")

def generate_component(path: str, name: str):
    if name[-1] == "/":
        create_folder(path, name)
    else: 
        create_file(path, name)

def generate_folder_structure(path: str, structure_dict: dict):
    for key in structure_dict:        
        if (structure_dict[key] == None):
            generate_component(path, key)
        else:
            generate_component(path, key)
            generate_folder_structure(f"{path}/{key}", structure_dict[key])

if __name__ in "__main__::":
    create_folder('.', 'my_project')
    generate_folder_structure("./my_project", file_structure)
