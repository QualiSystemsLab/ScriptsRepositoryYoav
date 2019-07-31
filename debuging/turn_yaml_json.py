import yaml
import json

def _populate_keys_as_json(yaml_file):
    yaml_keys = yaml_file.keys()
    yaml_dict = {}
    for key in yaml_keys:
        print key
        print yaml_file.get(key)
        try:
            yaml_dict.update({key: yaml_file.get(key)})
        except Exception as e:
            pass
    yaml_data_as_json_string = json.dumps(yaml_dict)
    return yaml_data_as_json_string

with open(r'c:\temp\new_vm.yml',"r") as f:
    result = f.read()
clean_result = result.split('# BEGIN ANSIBLE MANAGED BLOCK')[1].split('# END ANSIBLE MANAGED BLOCK')[0]
yaml_file = yaml.load(clean_result)
_populate_keys_as_json(yaml_file)
pass