#!/usr/bin/env python3

import sys
import os

# System test
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+"/pylib")
print(os.getcwd())
print("INFO Python Environment")
print(sys.version)

if sys.version_info[0] < 3:
    raise Exception("ERROR Python 3 required")

# ---------------------------------------------
# system modules
import time
import signal
import os
import psutil

# epics modules
import epics
print(epics.ca.find_libca())

# local functions
from genericlibs import *
from genericepics import *
from menu import *

# local runtime functions
import timnetdump
# =========================================

# Crush handler
process = psutil.Process(os.getpid())
# Add signal handler


def signal_term_handler(signal=None, frame=None):
    print("ERROR SIGTERM")
    print("ERROR ", sys.exc_info())
    print("ERROR process.memory_info().rss " + str(process.memory_info()))
    sys.exit(0)


signal.signal(signal.SIGTERM, signal_term_handler)

# CONFIGURATION

# Get the cli params
cli_params = menu()
param_file = cli_params["params"]
param_dump = cli_params["dump"]
# Get the start time
time_stamp_st = time2iso()
# declare meta list to log the program progress
meta_list = []

# Add globals into meta list
msg2meta("INFO time_stamp_st " + str(time_stamp_st), msg_list=meta_list)


def main():
    if param_dump:
        timnetdump.main("timsysd")


if __name__ == '__main__':
    try:
        main()
    except:
        signal_term_handler()

