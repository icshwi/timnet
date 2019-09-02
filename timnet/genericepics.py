#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import epics
import datetime
import math
import sys
import socket


def pv_info(pv_str, file=None, msg_list=[]):
    tmp = pv_str
    pv_tmp = epics.PV(tmp)
    msg = "INFO " + str(tmp) + ' ' + str(pv_tmp.value)
    msg_list.append(msg)
    print(msg, file=file)
    return pv_tmp.value


def pv_error(pv_str, valid, msg_list=[]):
    tmp = pv_str
    pv_tmp = epics.PV(tmp)
    msg = str(tmp) + ' ' + str(pv_tmp.value)
    if round(pv_tmp.value) != valid:
        msg = "ERROR " + msg
    else:
        msg = "INFO " + msg
    msg_list.append(msg)
    print(msg)
    return pv_tmp.value


# def pv_output(pv_str, file=None):
#     tmp = pv_str
#     pv_tmp = epics.PV(tmp)
#     print(pv_tmp.value, file=file)
#     return pv_tmp.value


def pv_write(pv_str, value):
    tmp = pv_str
    pv_tmp = epics.PV(tmp)
    pv_tmp.put(value)
    return pv_tmp.get()

