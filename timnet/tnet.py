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
# START
# =========================================


def tim_net_id_read(ioc_str, tim_net_json):
    for pv_str in netpvs:
        if "EVR" in ioc_str:
            dev_type = "EVR"
        else:
            dev_type = "EVM"

        pv_str_tmp = netpvs[pv_str][dev_type]
        if pv_str_tmp != "":
            eps_req_str = ioc_str + pv_str_tmp
            pv_val_tmp = epics.PV(eps_req_str, connection_timeout=1).value
        else:
            pv_val_tmp = ""

        if pv_val_tmp != "":
            if pv_val_tmp is not None:
                tim_net_json[ioc_str].update({pv_str: pv_val_tmp})
            else:
                tim_net_json[ioc_str].update({"state": "FAULT"})
                break


def main(inventory_jl, network_jl, pvs_jl):
    global netpvs
    logging.info(__file__)
    # Get the script root location
    # root = __file__.replace(os.path.basename(__file__), "")
    # root = "."
    with open(pvs_jl) as infile:
        netpvs = json.load(infile)

    with open(inventory_jl) as infile:
        tim_net_json = json.load(infile)

    for ioc_str in tim_net_json:
        tim_net_id_read(ioc_str, tim_net_json)

    with open(network_jl, 'w') as outfile:
        json.dump(tim_net_json, outfile)

    logging.info(tim_net_json)


if __name__ == '__main__':
    main()

