#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import json
import hjson

from genericlibs import *
from string import digits


# Remove not necessary digits from strings - comparison purposes
# def rm_dig(arg_str):
#     #return ''.join(filter(lambda x: x.isalpha(), arg_str))
#     return ''.join(filter(lambda x: not x.isdigit(), arg_str))


def assert_check(check, network):
    if 'eq' in check:
        if check["eq"] != network:
            return "ERROR EQ " + str(check["eq"]) + "!=" + str(network)
    if 'neq' in check:
        if check["neq"] == network:
            return "ERROR NEQ " + str(check["neq"]) + "==" + str(network)
    # Ignore negative values (they are not set)
    # network == 0 if it is not connected
    if "min" in check and network > 0:
        if check["min"] > network:
            return "ERROR MIN " + str(check["min"]) + ">" + str(network)
    if "max" in check and network > 0:
        if check["max"] < network:
            return "ERROR MAX " + str(check["max"]) + "<" + str(network)


def check_network(limits_json, network_json):
    _result_dict = {}
    for devi_str in limits_json:
        for prefix_str in network_json:
            if devi_str in prefix_str:
                for pvi_str in network_json[prefix_str]:
                    for pv_check_str in limits_json[devi_str]:
                        #assert_check(rec_check_str, rec_net_str, check_json, network_json[prefix_str])
                        #if pv_check_str == rm_dig(pvi_str):
                        if pv_check_str == pvi_str:
                            result_tmp = assert_check(limits_json[devi_str][pv_check_str], network_json[prefix_str][pvi_str])
                            if result_tmp:
                                dict2d_append(_result_dict, [prefix_str, pvi_str, result_tmp])

    return _result_dict


def main(network_jl, limits_jl, output_jl):
    logging.info(__file__)

    with open(network_jl) as infile:
        network_json = json.load(infile)

    with open(limits_jl) as infile:
        limits_json = hjson.load(infile)

    out = check_network(limits_json, network_json)

    with open(output_jl, 'w') as outfile:
        outfile.write(json.dumps(out, indent=4))

    logging.info(out)


if __name__ == '__main__':
    main()

