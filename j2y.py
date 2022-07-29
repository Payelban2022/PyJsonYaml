import sys
print(sys.version)
import json
import yaml

with open('input/donuts.json') as j:
    with open("output/donuts.yaml",'w')as y:
        json_data = json.loads(j.read())
        converted_json_data = json.dumps(json_data)
        yaml_data = yaml.safe_load(converted_json_data)
        converted_yaml_data = yaml.dump(yaml_data,indent=2)
        y.write(converted_yaml_data)

with open('input/emojis.json') as j1:
    with open("output/emojis.yaml",'w')as y1:
        json_data = json.loads(j1.read())
        converted_json_data = json.dumps(json_data)
        yaml_data = yaml.safe_load(converted_json_data)
        converted_yaml_data = yaml.dump(yaml_data,indent=2)
        y1.write(converted_yaml_data)
