import judge

class Model:
    def understand(script):
        return judge.Toolkit.get_bang(script)

    def clean(what):
        if what is not None:
            judge.Toolkit.delete(what)

    def extend(language):
        return judge.Toolkit.extend(language)

    def save_script(where, what):
        judge.Toolkit.save(where, what)
