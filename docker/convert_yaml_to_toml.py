# yaml_to_toml.py

import sys
import yaml
import toml

def convert_yaml_to_toml(yaml_file, toml_file):
    # Load the YAML content
    with open(yaml_file, 'r') as f:
        yaml_content = yaml.safe_load(f)

    # Convert to TOML format and save
    with open(toml_file, 'w') as f:
        toml.dump(yaml_content, f)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python yaml_to_toml.py <input_file.yaml> <output_file.toml>")
    else:
        convert_yaml_to_toml(sys.argv[1], sys.argv[2])

