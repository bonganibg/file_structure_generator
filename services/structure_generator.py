from services.file_access import FileAccess

class StructureGenerator():

    def __init__(self, file_access: FileAccess) -> None:
        self.file_access = file_access

    def generate_component(self, path: str, name: str):
        if name[-1] == "/":
            self.file_access.create_folder(path, name)
        else: 
            self.file_access.create_file(path, name)

    def generate_folder_structure(self, path: str, structure_dict: dict):
        for key in structure_dict:        
            if (structure_dict[key] == None):
                self.generate_component(path, key)
            else:
                self.generate_component(path, key)
                self.generate_folder_structure(f"{path}/{key}", structure_dict[key])            

    