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


def _evm_add_rx(_dev, tim_net_json, prefix_str):
    _dev["rx1"] = tim_net_json[prefix_str]["SFP1-Pwr-RX-I"]
    _dev["rx2"] = tim_net_json[prefix_str]["SFP2-Pwr-RX-I"]
    _dev["rx3"] = tim_net_json[prefix_str]["SFP3-Pwr-RX-I"]
    _dev["rx4"] = tim_net_json[prefix_str]["SFP4-Pwr-RX-I"]
    _dev["rx5"] = tim_net_json[prefix_str]["SFP5-Pwr-RX-I"]
    _dev["rx6"] = tim_net_json[prefix_str]["SFP6-Pwr-RX-I"]
    _dev["rx7"] = tim_net_json[prefix_str]["SFP7-Pwr-RX-I"]
    _dev["rx8"] = tim_net_json[prefix_str]["SFP8-Pwr-RX-I"]
    if 0 == _dev["rx1"]:
        del _dev["rx1"]
    if 0 == _dev["rx2"]:
        del _dev["rx2"]
    if 0 == _dev["rx3"]:
        del _dev["rx3"]
    if 0 == _dev["rx4"]:
        del _dev["rx4"]
    if 0 == _dev["rx5"]:
        del _dev["rx5"]
    if 0 == _dev["rx6"]:
        del _dev["rx6"]
    if 0 == _dev["rx7"]:
        del _dev["rx7"]
    if 0 == _dev["rx8"]:
        del _dev["rx8"]


def net_node_add(prefix_str, tim_net_json, level):
    # print(tim_net_json[prefix_str]["ID"][-2])
    _id_int = int(tim_net_json[prefix_str]["ID"])
    _id_hex_str = tim_net_json[prefix_str]["ID"][::-1]

    if "EVR" in prefix_str:
        _dev = evr_const.copy()
        _dev["rx"] = tim_net_json[prefix_str]["SFP-Pwr-RX-I"]
    else:
        _dev = evm_const.copy()
        _evm_add_rx(_dev, tim_net_json, prefix_str)

    _dev["dev"] = prefix_str
    _dev["id"] = hex2short(tim_net_json[prefix_str]["ID"])

    if _id_int < 0:
        net_plot_nc[_dev["dev"]] = _dev.copy()
        return -1

    if int(_id_hex_str[level]) != 0 and int(_id_hex_str[level+1]) == 0:
        if {} == net_plot[int(_id_hex_str[level])]:
            net_plot[int(_id_hex_str[level])] = _dev.copy()
        elif {} == net_plot[int(_id_hex_str[level])][int(_id_hex_str[level-1])]:
            net_plot[int(_id_hex_str[level])][int(_id_hex_str[level-1])] = _dev.copy()
        elif {} == net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])]:
            net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])] = _dev.copy()
        elif {} == net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])]:
            net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])] = _dev.copy()
        elif {} == net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])][int(_id_hex_str[level - 4])]:
            net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])][int(_id_hex_str[level - 4])] = _dev.copy()
        elif {} == net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])][int(_id_hex_str[level - 4])][int(_id_hex_str[level - 5])]:
            net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])][int(_id_hex_str[level - 4])][int(_id_hex_str[level - 5])] = _dev.copy()
        elif {} == net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])][int(_id_hex_str[level - 4])][int(_id_hex_str[level - 5])][int(_id_hex_str[level - 6])]:
            net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])][int(_id_hex_str[level - 4])][int(_id_hex_str[level - 5])][int(_id_hex_str[level - 6])] = _dev.copy()
        elif {} == net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])][int(_id_hex_str[level - 4])][int(_id_hex_str[level - 5])][int(_id_hex_str[level - 6])][int(_id_hex_str[level - 7])]:
            net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])][int(_id_hex_str[level - 4])][int(_id_hex_str[level - 5])][int(_id_hex_str[level - 6])][int(_id_hex_str[level - 7])] = _dev.copy()
        elif {} == net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])][int(_id_hex_str[level - 4])][int(_id_hex_str[level - 5])][int(_id_hex_str[level - 6])][int(_id_hex_str[level - 7])][int(_id_hex_str[level - 8])]:
            net_plot[int(_id_hex_str[level])][int(_id_hex_str[level - 1])][int(_id_hex_str[level - 2])][int(_id_hex_str[level - 3])][int(_id_hex_str[level - 4])][int(_id_hex_str[level - 5])][int(_id_hex_str[level - 6])][int(_id_hex_str[level - 7])][int(_id_hex_str[level - 8])] = _dev.copy()
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
            _evm_add_rx(evm_tmp, tim_net_json, prefix_str)
            net_plot.update(evm_tmp)
            break

    if net_plot == {}:
        raise Exception("ERROR EVG not detected")

    # Build the network plot
    for lv in range(0, 8):
        for prefix_str in tim_net_json:
            net_node_add(prefix_str, tim_net_json, lv)

    with open(plot_jl, 'w') as outfile:
        #json.dump({**net_plot, **net_plot_nc}, outfile)
        outfile.write(json.dumps({**net_plot, **net_plot_nc}, indent=4))

    logging.info(net_plot)


if __name__ == '__main__':
    main()

