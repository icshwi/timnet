#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from anytree import Node, RenderTree

# local functions
from genericlibs import *
from genericepics import *
# local runtime functions

# =========================================
# Program variables

# START
# =========================================
# Add globals into meta list


def main(args={}, interface={}):
    print("INFO", __file__)

    with open(interface["dir"]+interface["output"]) as infile:
        tim_sys_json = json.load(infile)

    for timsys_el in tim_sys_json:
        tim_sys_json[timsys_el]["ID"] = format(tim_sys_json[timsys_el]["ID"], "08x")

    # find EVG
    for timsys_el in tim_sys_json:
        if tim_sys_json[timsys_el]["ID"] == "0"*8:
            tim_sys_json[timsys_el].update({"pynode": None})
            tim_sys_json[timsys_el]["pynode"] = Node(timsys_el)
            evg_ref = tim_sys_json[timsys_el]
            break

    # first level nodes
    for timsys_el in tim_sys_json:
        if tim_sys_json[timsys_el]["ID"][:-1] == "0" * 7:
            tim_sys_json[timsys_el].update({"pynode": Node(timsys_el, parent=evg_ref["pynode"])})
        #print(timsys_el)

    print(tim_sys_json)

    for pre, fill, node in RenderTree(evg_ref["pynode"]):
        print("%s%s" % (pre, node.name))


if __name__ == '__main__':
    main()

