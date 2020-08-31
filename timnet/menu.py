#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from genericlibs import *
import argparse


def menu():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", action="count", default=0)
    parser.add_argument("-n", "--net", action='store_true', help="Read the current network topology via Epics.")
    parser.add_argument("-p", "--plot", action='store_true', help="Plot the actual network topology.")
    parser.add_argument("-d", "--dev", action='store_true', help="Apply devel settings - *_dev files.")
    parser.add_argument("-c", "--check", action='store_true', help="Checks the timing network anomalies.")
    parser.add_argument("-m", "--manual", action='store_true', help="Print the application manual.")
    parser.add_argument("--pvs", action='store', default="inventory/pvs.json", help="Use this PV set for the network evaluation.")
    parser.add_argument("-i", "--inventory", action='store', default="inventory/example.json", help="Network inventory with the PV prefixes.")
    args = parser.parse_args()
    if args.verbosity >= 2:
        print("Running '{}'".format(__file__))
    if args.verbosity >= 1:
        print(args)
    #return {"net": args.net, "plot": args.plot, "dev": args.dev, "manual": args.manual, "check": args.check}
    return args


if __name__ == '__main__':
    args = menu()
    print(args)
    print(args.check)
