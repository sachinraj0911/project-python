## dupms a file into python object using json
import json

filename = 'text.txt'

commands = {}
with open(filename, 'r') as fh:
    for line in fh:
        command, description = line.strip().split(' ' , 1)
        commands[command] = description.strip()

print(json.dumps(commands, indent=2, sort_keys=True))

