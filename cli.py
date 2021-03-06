import judge
import sys
import os

def parse_args(args):
    args = sys.argv[1:]
    if len(args) <= 1:
        return None
    return {
        'src': args[0],
        'txt': args[1],
    }

def run(params):
    pipe = params['src']
    inlet = params['txt']
    bot = judge.Judge(pipe, inlet)

    if (bot.raw_config is None) and ('JOEDGEBOT_HOME' in os.environ):
        bot.set_config(os.environ['JOEDGEBOT_HOME'])

    outlet, elapsed = bot.run()
    if type(outlet) is type(b''):
        outlet = outlet.decode('utf-8')
    return outlet

if __name__ == '__main__':
    params = parse_args(sys.argv)
    print('Arguments missing!' if not params else run(params))
