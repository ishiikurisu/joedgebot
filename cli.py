import judge
import sys

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
    outlet, elapsed = bot.run()
    return outlet

if __name__ == '__main__':
    params = parse_args(sys.argv)
    print('Arguments missing!' if not params else run(params))
