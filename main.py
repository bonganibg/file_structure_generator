import os 
from typing import List
import json

'''
Step 2: A bit more advanced

Still needs some exception handling in certain places
'''

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

def get_template_names():
    if (os.path.exists("templates")):
        return os.listdir("templates")
    
    return []

def display_options(templates: List[str]):    
    if len(templates) == 0:
        print("No templates found")
        return
    
    print("Which template would you like to use: ")

    for index, template in enumerate(templates, start=1):
        print(f"{index}. {template}")

def get_template(path: str, file_name: str) -> dict:
    with open(f"{path}/{file_name}", "r") as file:
        return json.load(file)
    

if __name__ in "__main__:":
    TEMPLATE_PATH = "templates"    

    templates = get_template_names()

    # Display menu and get the users choice
    display_options(templates)
    template_choice = int(input(">> "))

    # Validate that the value is in the correct range 
    if (template_choice < 1 or template_choice > len(templates)):
        print("Invalid choice")
        exit()

    # Get the template    
    template_name = templates[template_choice - 1]
    template_structure = get_template(TEMPLATE_PATH, template_name)

    # Get folder path for new project
    path = input("Enter the path for the new project: ")
    project_name = input("Enter the name of the project: ")

    create_folder(path, project_name)

    # Generate the template
    generate_folder_structure(f"{path}/{project_name}", template_structure)



