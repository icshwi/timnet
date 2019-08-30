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
    "MTCA5U-EVG": {},
    "MTCA5U-EVR": {},
    "MTCA5U-EVR1": {}
    # "MTCA5U-EVR2",
}

timsyspvs = {
    "ID": {"EVR": "DC-ID-I", "EVM": "FCT-ID-I"},
    "HwType": {"EVR": "HwType-I", "EVM": ""},
    "FwVer": {"EVR": "FwVer-I", "EVM": "FwVer-I"},
    "SwVer": {"EVR": "SwVer-I", "EVM": "SwVer-I"},
    "Ena-Sel": {"EVR": "Ena-Sel", "EVM": "Enable-Sel"},
    "Pll-Sts": {"EVR": "Pll-Sts", "EVM": "EvtClk-Pll-Sts"},
    "Time": {"EVR": "Time-I", "EVM": ""},
    "Time-Valid": {"EVR": "Time-Valid-Sts", "EVM": ""},
    "Pos": {"EVR": "Pos-I", "EVM": ""},

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

    "Link-Sts": {"EVR": "Link-Sts", "EVM": "U:Link-Sts"},
    "FCT-Link1-Sts": {"EVR": "", "EVM": "FCT-Link1-Sts"},
    "FCT-Link2-Sts": {"EVR": "", "EVM": "FCT-Link2-Sts"},
    "FCT-Link3-Sts": {"EVR": "", "EVM": "FCT-Link3-Sts"},
    "FCT-Link4-Sts": {"EVR": "", "EVM": "FCT-Link4-Sts"},
    "FCT-Link5-Sts": {"EVR": "", "EVM": "FCT-Link5-Sts"},
    "FCT-Link6-Sts": {"EVR": "", "EVM": "FCT-Link6-Sts"},
    "FCT-Link7-Sts": {"EVR": "", "EVM": "FCT-Link7-Sts"},
    "FCT-Link8-Sts": {"EVR": "", "EVM": "FCT-Link8-Sts"},
}

# START
# =========================================
# Add globals into meta list


def tim_net_id_read(sys_str, timsys_obj):
    for timpv_str in timsyspvs:
        if "EVR" in sys_str:
            dev_type = "EVR"
        else:
            dev_type = "EVM"

        pv_str_tmp = timsyspvs[timpv_str][dev_type]
        if pv_str_tmp != "":
            if ':' in pv_str_tmp:
                pv_val_tmp = epics.PV(sys_str + pv_str_tmp).value
            else:
                pv_val_tmp = epics.PV(sys_str + ":" + pv_str_tmp).value
        else:
            pv_val_tmp = ""

        if pv_val_tmp != "":
            timsys_obj[sys_str].update({timpv_str: pv_val_tmp})


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

    for sys_str in timsys_json:
        tim_net_id_read(sys_str, timsys_json)

    with open(DIRFILE+OUTPUTFILE, 'w') as outfile:
        json.dump(timsys_json, outfile)

    print(timsys_json)


if __name__ == '__main__':
    main()

