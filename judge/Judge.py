import os

class Judge:
    def __init__(self, src_script, src_txt):
        """Creates a new judge that is able to run"""
        self.src_script = src_script
        self.src_txt = src_txt
        with open(src_script, 'r') as fp:
            self.script = fp.read()
        with open(src_txt, 'r') as fp:
            self.txt = fp.read()

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
        # TODO Add this data to a JSON file for better processing
        if extension == 'py':
            return 'python'
        elif extension == 'rb':
            return 'ruby'
        elif extension == 'java':
            return 'java'
        elif extension == 'c':
            return 'c'
        else:
            raise TypeError()
