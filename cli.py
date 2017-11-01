import judge
import sys

def parse_args(args):
    args = sys.argv[1:]
    if len(args) <= 1:
        return None
    return 'hello joe!'

if __name__ == '__main__':
    params = parse_args(sys.argv)
    if not params:
        print('Arguments missing!')
    else:
        print('hello joe!')
