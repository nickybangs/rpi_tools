import json
import sys
JSON_PATH = sys.prefix
with open(f'{JSON_PATH}/ftp.json') as f:
    default = json.load(f)
