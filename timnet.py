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

# =========================================

# CONFIGURATION

# Get the cli params
cli_params = menu()
params_file = cli_params["params"]
# Get the start time
time_stamp_st = time2iso()
# declare meta list to log the program progress
meta_list = []

# Test object
TIMSYS = {
    "MTCA5U-EVG": {"type": "EVM", "value": 0},
    "MTCA5U-EVR": {"type": "EVR", "value": 0},
    "MTCA5U-EVR1": {"type": "EVR", "value": 0},
    # "MTCA5U-EVR2": {"type": "EVR", "value": 0},
}

# The file containing all the timing devices in the TIMSYS format
if params_file == "True":
    exec(open("params.py").read())
# START
# =========================================
# Add globals into meta list
msg2meta("INFO time_stamp_st " + str(time_stamp_st), msg_list=meta_list)

process = psutil.Process(os.getpid())
# Add signal handler


def signal_term_handler(signal=None, frame=None):
    print("ERROR SIGTERM Detected")
    print("ERROR ", sys.exc_info())
    print("ERROR process.memory_info().rss " + str(process.memory_info()))
    sys.exit(0)


signal.signal(signal.SIGTERM, signal_term_handler)


def tim_net_id_read(pv_str, timsys_obj):
    if timsys_obj[pv_str]["type"] == "EVR":
        pv_val_tmp = epics.PV(pv_str + ":" + "DC-ID-I").value
    else:
        pv_val_tmp = epics.PV(pv_str + ":" + "FCT-ID-I").value
    timsys_obj[pv_str]["value"] = pv_val_tmp


def main():
    output = open("out/output.timnet", "w")
    for pv_str in TIMSYS:
        tim_net_id_read(pv_str, TIMSYS)

    print(TIMSYS, file=output)
    output.close()


if __name__ == '__main__':
    try:
        main()
    except:
        signal_term_handler()

