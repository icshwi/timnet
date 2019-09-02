#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from genericlibs import *
import argparse


def menu():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    parser.add_argument("-n", "--net", action='store_true', help="Get the current network topology")
    parser.add_argument("-p", "--plot", action='store_true', help="Plot the network topology from the file")
    parser.add_argument("-d", "--dev", action='store_true', help="Apply devel settings")
    args = parser.parse_args()
    if args.verbosity >= 2:
        print("Running '{}'".format(__file__))
    if args.verbosity >= 1:
        print(args)
    return {"net": args.net, "plot": args.plot, "dev": args.dev}
