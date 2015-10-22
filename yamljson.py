#!/usr/bin/env python

import yaml
import json

def main():

    my_list = range(8)
    my_list.append('0 through 7 are cool numbers')
    my_list.append({})
    my_list[-1]['subnet_mask'] = '255.255.255.0'
    my_list[-1]['gateway'] = '192.168.1.1'

    with open("first_yaml_file.yml", "w") as f:
        f.write(yaml.dump(my_list, default_flow_style=False))

    with open("first_json_file.json", "w") as g:
        json.dump(my_list, g)



if __name__ == "__main__":
    main() 
