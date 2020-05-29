#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import json
from string import digits


# Remove not necessary digits from strings - comparison purposes
def rm_dig(arg_str):
    #return ''.join(filter(lambda x: x.isalpha(), arg_str))
    return ''.join(filter(lambda x: not x.isdigit(), arg_str))


def assert_check(check, network):
    # print(check, network)
    if 'eq' in check:
        if check["eq"] == network:
            return 0
        else:
            return "ERROR EQ " + str(check["eq"]) + "!=" + str(network)
    # network == 0 if the socket is not connected
    if check["min"] < network or network == 0:
        if check["max"] > network:
            return 0
        else:
            return "ERROR MAX " + str(check["max"]) + "<" + str(network)
    else:
        return "ERROR MIN " + str(check["min"]) + ">" + str(network)


def check_network(check_json, network_json):
    output = []
    for ioc_str in network_json:
        for rec_net_str in network_json[ioc_str]:
            for rec_check_str in check_json:
                #assert_check(rec_check_str, rec_net_str, check_json, network_json[ioc_str])
                if rec_check_str == rm_dig(rec_net_str):
                    result_tmp = assert_check(check_json[rec_check_str], network_json[ioc_str][rec_net_str])
                    if result_tmp != 0:
                        result_dict_tmp = [ioc_str, rec_net_str, result_tmp]
                        output.append(result_dict_tmp)
    return output


def main(network_jl, limits_jl, output_jl="json/errors_dev.json"):
    logging.info(__file__)

    with open(network_jl) as infile:
        network_json = json.load(infile)

    with open(limits_jl) as infile:
        limits_json = json.load(infile)

    out = check_network(limits_json, network_json)

    with open(output_jl, 'w') as outfile:
        json.dump(out, outfile)

    logging.info(out)


if __name__ == '__main__':
    main()

