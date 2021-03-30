import sys
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str, default='There is no path', help='This is the file path')
arg_obj = parser.parse_args()
path = arg_obj.path
print(path)


with open(path) as file_ob:
    data_json = json.load(file_ob)

print(data_json)