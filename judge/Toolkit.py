import os
import json

def load_config(configfile):
    outlet = { }
    with open('config.json', 'r') as fp:
        outlet = json.loads(fp.read())
    return outlet

def save(where, what):
    """Saves data on a file. Might overwrite any changes."""
    with open(where, 'w') as fp:
        fp.write(what)

def delete(what):
    """Removes the given file from the file system."""
    try:
        os.remove(what)
    except FileNotFoundError:
        pass

def identify(filename):
    """Identifies which language the script was written on."""
    extension = filename.split('.')[-1]
    raw_config = load_config('config.json')

    if extension in raw_config['available']:
        return raw_config['available'][extension]
    else:
        raise TypeError()

def get_bang(filename):
    # TODO Implement this function
    return 'python'