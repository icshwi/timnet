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
    1: {},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
    8: {},
}

evr_const = {
    "dev": "",
    "id": "",
}

net_plot = {}
net_plot_nc = {}


def net_node_add(prefix_str, tim_net_json, level):
    # print(tim_net_json[prefix_str]["ID"][-2])
    _id_int = int(tim_net_json[prefix_str]["ID"])
    _id_hex_str = tim_net_json[prefix_str]["ID"][::-1]

    if "EVR" in prefix_str:
        _dev = evr_const.copy()
    else:
        _dev = evm_const.copy()
    _dev["dev"] = prefix_str
    _dev["id"] = hex2short(tim_net_json[prefix_str]["ID"])

    if _id_int < 0:
        net_plot_nc[_dev["dev"]] = _dev.copy()
        return -1

    if int(_id_hex_str[level]) != 0 and int(_id_hex_str[level+1]) == 0:
        if net_plot[int(_id_hex_str[level])] == {}:
            net_plot[int(_id_hex_str[level])] = _dev.copy()
        else:
            net_plot[int(_id_hex_str[level])][int(_id_hex_str[level-1])] = _dev.copy()
        _dev.clear()


def del_none(d):
    for k, v in dict(d).items():
        if v is None:
            del d[k]


def hex2short(arg_str):
    return hex(int(arg_str, 16))


def main(network_jl, plot_jl):
    logging.info(__file__)

    with open(network_jl) as infile:
        tim_net_json = json.load(infile)

    for prefix_str in tim_net_json:
        for pvi_str in tim_net_json[prefix_str]:
            if "-ID-I" in pvi_str:
                tim_net_json[prefix_str]["ID"] = format(tim_net_json[prefix_str][pvi_str], "09x")
                break

    # Find EVG
    for prefix_str in tim_net_json:
        if int(tim_net_json[prefix_str]["ID"]) == 0:
            evm_tmp = evm_const
            evm_tmp["dev"] = prefix_str
            evm_tmp["id"] = hex2short(tim_net_json[prefix_str]["ID"])
            net_plot.update(evm_tmp)
            break

    if net_plot == {}:
        raise Exception("ERROR EVG not detected")

    # Build the network plot
    for lv in range(0, 8):
        for prefix_str in tim_net_json:
            net_node_add(prefix_str, tim_net_json, lv)

    with open(plot_jl, 'w') as outfile:
        json.dump({**net_plot, **net_plot_nc}, outfile)

    logging.info(net_plot)


if __name__ == '__main__':
    main()

