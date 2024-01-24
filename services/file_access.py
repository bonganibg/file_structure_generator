import os
import json


class FileAccess:

    def create_folder(self, path: str, folder_name: str):
        # Make sure that the folder does not exist already
        if os.path.exists(f"{path}/{folder_name}"):
            return
        
        os.mkdir(f"{path}/{folder_name}")


    def create_file(self, path: str, file_name: str):        
        with open(f"{path}/{file_name}", "w") as file:
            file.write("")

    def get_templates(self, template_path: str) -> dict:
        if (os.path.exists(template_path)):
            with open(template_path, "r") as file:
                return json.load(file)
            
        return None