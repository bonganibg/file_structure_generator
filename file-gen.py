import os 
import argparse
from typing import List
from services.file_access import FileAccess
from services.structure_generator import StructureGenerator

TEMPLATES_PATH = "templates.json"
__file_access = FileAccess()

'''
Step 3: Advanced command line tool
'''

def display_options(options: List[str]):

    for i, option in enumerate(options):
        print(f"O {option}")

def check_user_input():
    # Get the input based on the arguments that the user passed when running the application
    ...

def get_user_arguments():
    # Get the user arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--template", help="Template to create file structure from")
    parser.add_argument("-n", "--name", help="Name of new project to be generated", default="")
    # parser.add_argument("-l", "--list", help="Show the full list of templates")
    
    args = parser.parse_args()

    return args.template, args.name

def generate_template(project_name: str, template: dict):    
    structure_generator = StructureGenerator(__file_access)        

    # Create the project folder
    __file_access.create_folder(".", project_name)

    try:
        structure_generator.generate_folder_structure(project_name, template)
    except:
        print(f"Error with the template for {project_name}")
        exit()


if __name__ in "__main__:":    
    templates = __file_access.get_templates(TEMPLATES_PATH)
    template_name, project_name = get_user_arguments()    

    if (template_name == None):
        print("No template name provided")
        exit()

    if template_name not in templates.keys():
        print("Template not found")
        exit()
    
    generate_template(template_name, templates[template_name])
