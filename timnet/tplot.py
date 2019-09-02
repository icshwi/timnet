#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import logging

# local functions
from genericlibs import *
from genericepics import *
# local runtime functions

# Objects
evm_const = {
    "dev": "",
    "id": "",
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None
}

evr_const = {
    "dev": "",
    "id": ""
}

net_plot = {}


def net_node_add(ioc_str, tim_net_json, level):
    # print(tim_net_json[ioc_str]["ID"][-2])
    id_tmp = tim_net_json[ioc_str]["ID"][::-1]
    if int(id_tmp[level]) != 0 and int(id_tmp[level+1]) == 0:
        if "EVR" in ioc_str:
            dev_tmp = evr_const
        else:
            dev_tmp = evm_const
        dev_tmp["dev"] = ioc_str
        dev_tmp["id"] = tim_net_json[ioc_str]["ID"]
        if net_plot[int(id_tmp[level])] is None:
            net_plot[int(id_tmp[level])] = dev_tmp
        else:
            net_plot[int(id_tmp[level])][int(id_tmp[level-1])] = dev_tmp


def del_none(d):
    for k, v in dict(d).items():
        if v is None:
            del d[k]


def main(args={}, interface={}):
    logging.info(__file__)

    with open(interface["dir"]+interface["network"]) as infile:
        tim_net_json = json.load(infile)

    for ioc_str in tim_net_json:
        tim_net_json[ioc_str]["ID"] = format(tim_net_json[ioc_str]["ID"], "08x")

    # Find EVG
    for ioc_str in tim_net_json:
        if int(tim_net_json[ioc_str]["ID"]) == 0:
            evm_tmp = evm_const
            evm_tmp["dev"] = ioc_str
            evm_tmp["id"] = tim_net_json[ioc_str]["ID"]
            net_plot.update(evm_tmp)
            break

    # Build the network plot
    for lv in range(0, 8):
        for ioc_str in tim_net_json:
            net_node_add(ioc_str, tim_net_json, lv)

    with open(interface["dir"]+interface["plot"], 'w') as outfile:
        json.dump(net_plot, outfile)

    logging.info(net_plot)


if __name__ == '__main__':
    main()

