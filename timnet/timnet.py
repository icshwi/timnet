#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from genericlibs import *
from genericepics import *
from menu import *

# Local runtime modules
import tnet
import tplot
# =========================================


def main():
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    # Assure py3
    assure_py3()
    # Check epics
    logging.info("epics " + str(epics.ca.find_libca()))
    # Get the cli params
    cli_params = menu()
    param_net = cli_params["net"]
    param_plot = cli_params["plot"]
    # Get the start time
    time_stamp_st = time2iso()
    # declare meta list to log the program progress

    input_file = "input.json"
    output_file = "output.json"
    json_dir = "json/"
    if "dev" in cli_params:
        input_file = input_file.replace(".json", "_dev.json")
        output_file = output_file.replace(".json", "_dev.json")

    interface = {"dir": json_dir, "input": input_file, "output": output_file}

    logging.info("cli_params " + str(cli_params))
    logging.info("interface " + str(interface))
    if param_net:
        tnet.main(cli_params, interface)
    if param_plot:
        tplot.main(cli_params, interface)


if __name__ == '__main__':
    main()
