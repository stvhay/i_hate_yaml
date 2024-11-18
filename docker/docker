# toml_to_yaml.py

import sys
import toml
import yaml

def convert_toml_to_yaml(toml_file, yaml_file):
    with open(toml_file, 'r') as f:
        toml_content = toml.load(f)
    
    with open(yaml_file, 'w') as f:
        yaml.dump(toml_content, f, default_flow_style=False)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python toml_to_yaml.py <input_file.toml> <output_file.yaml>")
    else:
        convert_toml_to_yaml(sys.argv[1], sys.argv[2])

