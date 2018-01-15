#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os.path
STUN_SOURCE_DIR = 'packages/pystun'
if os.path.exists(STUN_SOURCE_DIR):
    import sys
    sys.path.append(os.path.abspath(STUN_SOURCE_DIR))
import stun  # @see http://github.com/jtriley/pystun


def detect_network_type():
    nat_type, external_ip, external_port = stun.get_ip_info()
    if 'Blocked' == nat_type:
        print('Warning: Unable to connect to STUN server!')
        return
    if external_ip:
        print('Server-reflexive transport IP: Your public IP address is %s' % external_ip)
    if type(external_port) == int:
        print('Server-reflexive port: Your UDP port is %d' % external_port)
    if nat_type:
        print('Your NAT type: %s (may be)' % nat_type)
    return


if '__main__' == __name__:
    detect_network_type()
