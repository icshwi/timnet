#!/usr/bin/env python3

from genericlibs import *
import argparse


def menu():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    parser.add_argument("-p", "--params", type=str, default="False", help="[True False] Activates the 'params' file content which overwrites program settings")
    parser.add_argument("-d", "--dump", action='store_true', help="")
    args = parser.parse_args()
    if args.verbosity >= 2:
        print("Running '{}'".format(__file__))
    if args.verbosity >= 1:
        print(args)
    return {"params": args.params, "dump": args.dump}
