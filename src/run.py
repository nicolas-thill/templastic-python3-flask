#!/usr/bin/env python3

import atexit
import sys
import time
from signal import SIGINT, SIGTERM, signal

ME = sys.argv[0]


def _msg(m):
    print("%s: %s" % (ME, m), flush=True)


def _start(a):
    _msg("starting...")
    time.sleep(1)
    _msg("started!")
    signal(SIGINT, lambda signum, stack_frame: exit(1))
    signal(SIGTERM, lambda signum, stack_frame: exit(1))
    atexit.register(_stop)
    return True


def _loop():
    _msg("running...")
    while True:
        time.sleep(1)


def _stop():
    _msg("stopping...")
    time.sleep(1)
    _msg("stopped!")


if _start(sys.argv):
    _loop()
