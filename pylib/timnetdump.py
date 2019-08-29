#!/usr/bin/env python3
import os
# local functions
from genericlibs import *
from genericepics import *
# local runtime functions

# =========================================
# Program variables

# CONFIGURATION
# Test object
TIMSYS = {
    "MTCA5U-EVG": {"type": "EVM", "value": 0},
    "MTCA5U-EVR": {"type": "EVR", "value": 0},
    "MTCA5U-EVR1": {"type": "EVR", "value": 0},
    # "MTCA5U-EVR2": {"type": "EVR", "value": 0},
}

# START
# =========================================
# Add globals into meta list


def tim_net_id_read(pv_str, timsys_obj):
    if timsys_obj[pv_str]["type"] == "EVR":
        pv_val_tmp = epics.PV(pv_str + ":" + "DC-ID-I").value
    else:
        pv_val_tmp = epics.PV(pv_str + ":" + "FCT-ID-I").value
    timsys_obj[pv_str]["value"] = pv_val_tmp


def main(args=""):
    print("INFO", __file__)
    # Get the script root location
    root = __file__.replace(os.path.basename(__file__), "")

    if "timsysd" in args:
        exec(open(root+"/timsys.pyd").read())

    output = open("output.timnet", "w")
    for pv_str in TIMSYS:
        tim_net_id_read(pv_str, TIMSYS)

    print(TIMSYS, file=output)
    output.close()


if __name__ == '__main__':
    main()

