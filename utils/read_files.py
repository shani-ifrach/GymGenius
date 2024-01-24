import os.path
import yaml

def read_yaml_file(file_path):
    with open(file_path, 'r+') as file:
        # Load YAML content into a Python dictionary
        data = yaml.safe_load(file)
        return data


# Example usage:
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "params.yml")
yaml_data = read_yaml_file(file_path)
project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if yaml_data:
    print("YAML file content:")
    print(yaml_data)
