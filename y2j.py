import sys
print(sys.version)

import json
import yaml


with open('input/verify.yaml') as y:
    with open("output/verify.json",'w')as j:
        yaml_data = yaml.safe_load(y.read())
        converted_json_data = json.dumps(yaml_data,indent=2)


        j.write(converted_json_data)

with open('input/xmas.yaml') as y1:
    with open("output/xmas.json",'w')as j1:
        yaml_data = yaml.safe_load(y1.read())
        converted_json_data = json.dumps(yaml_data,indent=2)


        j1.write(converted_json_data)