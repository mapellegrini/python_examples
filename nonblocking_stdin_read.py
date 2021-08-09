#!/usr/bin/python3

import sys
import select
import time

def non_blocking_read(wait_time=60):
    """
    Poll stdin at one second intervals until input is read, or until s
    seconds have elapsed
    """
    assert(wait_time >= 0)
    elapsed = 0

    while elapsed < wait_time:
        time.sleep(1)
        elapsed += 1

        while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = sys.stdin.readline()
            if line:
                return line.strip()
            else: # an empty line means stdin has been closed
                pass
        else:  # no input was read
            pass
    return None

x = non_blocking_read(wait_time=6)
print("read ", x)
