import os 
from typing import List
from services.file_access import FileAccess
from services.structure_generator import StructureGenerator

'''
Step 3: Advanced command line tool
'''

def display_options(options: List[str]):

    for i, option in enumerate(options):
        print(f"O {option}")

def check_user_input():
    # Get the input based on the arguments that the user passed when running the application
    

if __name__ in "__main__:":
    TEMPLATES_PATH = "templates.json"

    file_access = FileAccess()
    structure_generator = StructureGenerator(file_access)


    # Load the templates data
    templates = file_access.get_templates(TEMPLATES_PATH)

    # Get the users template choice 
    display_options(templates.keys())
    template_choice = input("Enter your choice: ")

    # Check if the choice is valid
    if (template_choice not in templates.keys()):
        print("Invalid choice")
        exit()

    # Get the template data
    chosen_template = templates[template_choice]

    # Get the location of the project
    directory = input("Enter the directory of the project: ")
    project_name = input("Enter the name of the project: ")
    
    # Create the project folder
    file_access.create_folder(directory, project_name)
    
    # Generate the folder structure
    structure_generator.generate_folder_structure(f"{directory}/{project_name}", chosen_template)

