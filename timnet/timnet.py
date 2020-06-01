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

    # Get the cli params
    cli_params = menu()
    if cli_params.manual:
        print(open('README.md').read())

    # Interface
    interface = {"inventory": cli_params.inventory,
                 "network": cli_params.inventory.replace(".", "_net."),
                 "plot": cli_params.inventory.replace(".", "_plot."),
                 "limits": "inventory/limits.json",
                 "errors": cli_params.inventory.replace(".", "_err.")
                 }

    if cli_params.dev:
        for el in interface:
            interface[el] = interface[el].replace(".", "_dev.")

    # declare meta list to log the program progress
    logging.info("cli_params " + str(cli_params))
    logging.info("interface " + str(interface))
    if cli_params.net:
        tnet.main(inventory_jl=interface["inventory"], network_jl=interface["network"])
    if cli_params.plot:
        tplot.main(network_jl=interface["network"], plot_jl=interface["plot"])
    if cli_params.check:
        tcheck.main(network_jl=interface["network"], limits_jl=interface["limits"], output_jl=interface["errors"])


if __name__ == '__main__':
    main()
