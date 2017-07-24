import sys
from app import *

if __name__ == '__main__':
    api = sys.argv[1]
    bot = App(api)
    print('---')
    while True:
        try:
            bot.loop()
        except KeyboardInterrupt:
            print('...')
            break
#         except:
#             print('--- # Connection lost... restarting')
#             bot = App(api)
