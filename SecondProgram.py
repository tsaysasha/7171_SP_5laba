import threading
import time
from random import randint


def child_team():
    i = randint(1, 100)
    while i > 0:
        print(f'child team: {i}')
        time.sleep(0.5)
        i = i - randint(1, 10)
        i = i + randint(1, 10)


def parent_team():
    i = randint(1, 100)
    threading.Thread(target=child_team).start()
    while i > 0:
        print(f'parent team: {i}')
        time.sleep(0.5)
        i = i - randint(1, 10)
        i = i + randint(1, 10)


if __name__ == '__main__':
    parent = threading.Thread(target=parent_team)
    parent.start()