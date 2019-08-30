#!/usr/bin/env python3
import os
import json
# local functions
from genericlibs import *
from genericepics import *
# local runtime functions

# =========================================
# Program variables

# CONFIGURATION
INPUTFILE = "timsys_inventory.json"
OUTPUTFILE = "timsys.json"
DIRFILE = "json/"
# Test object
timsys_dev = {
    "MTCA5U-EVG": {"type": "EVM"},
    "MTCA5U-EVR": {"type": "EVR"},
    "MTCA5U-EVR1": {"type": "EVR"},
    # "MTCA5U-EVR2": {"type": "EVR", "value": 0},
}

timsyspvs = {
    "ID": {"EVR": "DC-ID-I", "EVM": "FCT-ID-I"},
    "HwType": {"EVR": "HwType-I", "EVM": ""},
    "FwVer": {"EVR": "FwVer-I", "EVM": "FwVer-I"},
    "SwVer": {"EVR": "SwVer-I", "EVM": "SwVer-I"},
    "SFP-T": {"EVR": "SFP-T-I", "EVM": ""},
    "SFP1-T": {"EVR": "", "EVM": "SFP1-T-I"},
    "SFP2-T": {"EVR": "", "EVM": "SFP2-T-I"},
    "SFP3-T": {"EVR": "", "EVM": "SFP3-T-I"},
    "SFP4-T": {"EVR": "", "EVM": "SFP4-T-I"},
    "SFP5-T": {"EVR": "", "EVM": "SFP5-T-I"},
    "SFP6-T": {"EVR": "", "EVM": "SFP6-T-I"},
    "SFP7-T": {"EVR": "", "EVM": "SFP7-T-I"},
    "SFP8-T": {"EVR": "", "EVM": "SFP8-T-I"},
    "SFP-Pwr-RX": {"EVR": "SFP-Pwr-RX-I", "EVM": ""},
    "SFP1-Pwr-RX": {"EVR": "", "EVM": "SFP1-Pwr-RX-I"},
    "SFP2-Pwr-RX": {"EVR": "", "EVM": "SFP2-Pwr-RX-I"},
    "SFP3-Pwr-RX": {"EVR": "", "EVM": "SFP3-Pwr-RX-I"},
    "SFP4-Pwr-RX": {"EVR": "", "EVM": "SFP4-Pwr-RX-I"},
    "SFP5-Pwr-RX": {"EVR": "", "EVM": "SFP5-Pwr-RX-I"},
    "SFP6-Pwr-RX": {"EVR": "", "EVM": "SFP6-Pwr-RX-I"},
    "SFP7-Pwr-RX": {"EVR": "", "EVM": "SFP7-Pwr-RX-I"},
    "SFP8-Pwr-RX": {"EVR": "", "EVM": "SFP8-Pwr-RX-I"},
    "SFP-Pwr-TX": {"EVR": "SFP-Pwr-TX-I", "EVM": ""},
    "SFP1-Pwr-TX": {"EVR": "", "EVM": "SFP1-Pwr-TX-I"},
    "SFP2-Pwr-TX": {"EVR": "", "EVM": "SFP2-Pwr-TX-I"},
    "SFP3-Pwr-TX": {"EVR": "", "EVM": "SFP3-Pwr-TX-I"},
    "SFP4-Pwr-TX": {"EVR": "", "EVM": "SFP4-Pwr-TX-I"},
    "SFP5-Pwr-TX": {"EVR": "", "EVM": "SFP5-Pwr-TX-I"},
    "SFP6-Pwr-TX": {"EVR": "", "EVM": "SFP6-Pwr-TX-I"},
    "SFP7-Pwr-TX": {"EVR": "", "EVM": "SFP7-Pwr-TX-I"},
    "SFP8-Pwr-TX": {"EVR": "", "EVM": "SFP8-Pwr-TX-I"},
}

# START
# =========================================
# Add globals into meta list


def tim_net_id_read(pv_str, timsys_obj):
    for timpv_str in timsyspvs:
        if timsyspvs[timpv_str][timsys_obj[pv_str]["type"]] != "":
            pv_val_tmp = epics.PV(pv_str + ":" + timsyspvs[timpv_str][timsys_obj[pv_str]["type"]]).value
        else:
            pv_val_tmp = ""

        if pv_val_tmp != "":
            timsys_obj[pv_str].update({timpv_str: pv_val_tmp})


def main(args=""):
    print("INFO", __file__)
    # Get the script root location
    # root = __file__.replace(os.path.basename(__file__), "")
    # root = "."

    if "timsysd" in args:
        with open(DIRFILE+INPUTFILE) as infile:
            timsys_json = json.load(infile)
    else:
        timsys_json = timsys_dev

    for pv_str in timsys_json:
        tim_net_id_read(pv_str, timsys_json)

    with open(DIRFILE+OUTPUTFILE, 'w') as outfile:
        json.dump(timsys_json, outfile)

    print(timsys_json)


if __name__ == '__main__':
    main()

