#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from genericlibs import *
from genericepics import *
from menu import *

# Local runtime modules
import tnet
import tplot
import tcheck
# =========================================


def main():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    # Assure py3
    assure_py3()
    # Check epics
    logging.info("epics " + str(epics.ca.find_libca()))

    # Interface
    interface = {"dir": "json/", "inventory": "inventory.json", "network": "network.json", "plot": "plot.json", "check": "check.json"}

    # Get the cli params
    cli_params = menu()
    if cli_params["manual"]:
        print(open('README.md').read())
    param_net = cli_params["net"]
    param_plot = cli_params["plot"]
    param_check = cli_params["check"]
    # declare meta list to log the program progress

    if cli_params["dev"] is True:
        for el in interface:
            interface[el] = interface[el].replace(".json", "_dev.json")

    logging.info("cli_params " + str(cli_params))
    logging.info("interface " + str(interface))
    if param_net:
        tnet.main(cli_params, interface)
    if param_plot:
        tplot.main(cli_params, interface)
    if param_check:
        tcheck.main(cli_params, interface)


if __name__ == '__main__':
    main()
