#!/usr/bin/env python3

from genericlibs import *
import argparse


def menu():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    parser.add_argument("-d", "--dump", action='store_true', help="Dump the current network topology")
    parser.add_argument("-p", "--plot", action='store_true', help="Plot the network topology from the file")
    args = parser.parse_args()
    if args.verbosity >= 2:
        print("Running '{}'".format(__file__))
    if args.verbosity >= 1:
        print(args)
    return {"dump": args.dump, "plot": args.plot}
