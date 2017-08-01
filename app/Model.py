import judge
import os.path

class Model:
    def understand(script):
        return judge.Toolkit.get_bang(script)

    def clean(what):
        if what is not None:
            judge.Toolkit.delete(what)

    def erase_user(user):
        os.system('rm %s*' % (user))

    def extend(language):
        return judge.Toolkit.extend(language)

    def save_script(where, what):
        judge.Toolkit.save(where, what)

    def run(script, text):
        joe = judge.Judge(script, text)
        output, elapsed = joe.run()
        return output, elapsed

    def check_existence(filename):
        if not os.path.isfile(filename):
            raise RuntimeError()
