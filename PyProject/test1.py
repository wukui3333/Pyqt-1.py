# --Python 3.10
# test1.py by：2023/7/22
# Author：WUKUI

import sys, time


def callback():
    print(f'this is test1.py')
    print(f'{sys.argv}')

def run():
    print(time.time())

if __name__ == '__main__':
    callback()
    while True:
        run()
        time.sleep(1)