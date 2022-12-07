import time
import os
from threading import Timer

i = 0


def timer(program):
    cmd = 'tasklist | findstr ' + program
    global i

    def count(msg):
        global i
        i += 1

    class TickTimer(Timer):
        def run(self):
            while not self.finished.wait(self.interval):
                self.function(*self.args, **self.kwargs)

    tick = TickTimer(1, count, [''])
    tick.start()
    while os.system(cmd) == 0:
        time.sleep(1)

    tick.cancel()

    return i
