#!/usr/bin/env python3

# System modules
import sys
import os
import signal
import psutil

# Epics modules
import epics

# Local modules
sys.path.append(os.getcwd())
sys.path.append(os.getcwd() + "/py")
from genericlibs import *
from genericepics import *
from menu import *

# Local runtime modules
import timnetdump
import timnetplot
# =========================================
# Assure py3
assure_py3()
# Check epics
print(epics.ca.find_libca())

# Crush handler
process = psutil.Process(os.getpid())
# Add signal handler


def signal_term_handler(signal=None, frame=None):
    print("ERROR SIGTERM")
    print("ERROR ", sys.exc_info())
    print("ERROR process.memory_info().rss ", process.memory_info())
    sys.exit(0)


signal.signal(signal.SIGTERM, signal_term_handler)

# CONFIGURATION

# Get the cli params
cli_params = menu()
param_dump = cli_params["dump"]
param_plot = cli_params["plot"]
# Get the start time
time_stamp_st = time2iso()
# declare meta list to log the program progress
meta_list = []

# Add globals into meta list
msg2meta("INFO time_stamp_st " + str(time_stamp_st), msg_list=meta_list)


def main():
    if param_dump:
        timnetdump.main("timsysd")
        #timnetdump.main("timsysd")
    elif param_plot:
        timnetplot.main()


if __name__ == '__main__':
    main()
    #try:
    #    main()
    #except:
    #    signal_term_handler()

