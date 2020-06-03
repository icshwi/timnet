#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import logging
# local functions
from genericlibs import *
from genericepics import *
# local runtime functions


def tim_net_id_read(prefix_str, tim_net_json):
    for devi_str in netpvs:
        if devi_str in prefix_str:
            for pvi_str in netpvs[devi_str]:
                _pv_str = prefix_str + pvi_str
                _pv_val = epics.PV(_pv_str, connection_timeout=1).value
                tim_net_json[prefix_str].update({pvi_str: _pv_val})


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

    for prefix_str in tim_net_json:
        tim_net_id_read(prefix_str, tim_net_json)

    with open(network_jl, 'w') as outfile:
        json.dump(tim_net_json, outfile)

    logging.info(tim_net_json)


if __name__ == '__main__':
    main()

