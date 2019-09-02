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

# CONFIGURATION
INPUTFILE = "timnet.json"
OUTPUTFILE = "test.txt"
DIRFILE = "json/"
# Test object

# START
# =========================================
# Add globals into meta list


def main(args=""):
    print("INFO", __file__)

    # with open(DIRFILE+INPUTFILE) as infile:
    #     timsys_json = json.load(infile)
    #
    # for timsys_el in timsys_json:
    #     timsys_json[timsys_el]["ID"] = format(timsys_json[timsys_el]["ID"], "08x")
    #
    # # find EVG
    # for timsys_el in timsys_json:
    #     if timsys_json[timsys_el]["ID"] == "0"*8:
    #         timsys_json[timsys_el].update({"pynode": None})
    #         timsys_json[timsys_el]["pynode"] = Node(timsys_el)
    #         evg_ref = timsys_json[timsys_el]
    #         break
    #
    # # first level nodes
    # for timsys_el in timsys_json:
    #     if timsys_json[timsys_el]["ID"][:-1] == "0" * 7:
    #         timsys_json[timsys_el].update({"pynode": Node(timsys_el, parent=evg_ref["pynode"])})
    #     #print(timsys_el)
    #
    # print(timsys_json)
    #
    # for pre, fill, node in RenderTree(evg_ref["pynode"]):
    #     print("%s%s" % (pre, node.name))


if __name__ == '__main__':
    main()

