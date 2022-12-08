import time
import os
from datetime import datetime


def timer(program):
    cmd = 'tasklist | findstr ' + program
    start = datetime.now()

    while os.system(cmd) == 0:
        time.sleep(3)

    delta = datetime.now() - start
    return delta
