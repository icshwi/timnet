#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import logging
# local functions
from genericlibs import *
from genericepics import *
# local runtime functions

# =========================================
# Program variables
netpvs = {
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


def tim_net_id_read(ioc_str, tim_net_json):
    for pv_str in netpvs:
        if "EVR" in ioc_str:
            dev_type = "EVR"
        else:
            dev_type = "EVM"

        pv_str_tmp = netpvs[pv_str][dev_type]
        if pv_str_tmp != "":
            #if ':' in pv_str_tmp:
            #    eps_req_str = ioc_str + pv_str_tmp
            #else:
            eps_req_str = ioc_str + ":" + pv_str_tmp
            pv_val_tmp = epics.PV(eps_req_str, connection_timeout=1).value
        else:
            pv_val_tmp = ""

        if pv_val_tmp != "":
            if pv_val_tmp is not None:
                tim_net_json[ioc_str].update({pv_str: pv_val_tmp})
            else:
                tim_net_json[ioc_str].update({"state": "FAULT"})
                break


def main(inventory_jl, network_jl):
    logging.info(__file__)
    # Get the script root location
    # root = __file__.replace(os.path.basename(__file__), "")
    # root = "."

    with open(inventory_jl) as infile:
        tim_net_json = json.load(infile)

    for ioc_str in tim_net_json:
        tim_net_id_read(ioc_str, tim_net_json)

    with open(network_jl, 'w') as outfile:
        json.dump(tim_net_json, outfile)

    logging.info(tim_net_json)


if __name__ == '__main__':
    main()

