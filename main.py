from server import ZeroMQServer
from client import ZeroMQClient
from fsm import FSM
import sys

import os, sys

currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
if rootDir not in sys.path: # add parent dir to paths
    sys.path.append(rootDir)

from rpc.server import ZeroMQServer
from rpc.controller.na_cpg import NaCPG, create_fully_connected_adjacency
import torch
import matplotlib.pyplot as plt
# from SerTest import SerTestClass
import time
import math
import pdb
# import cv2
import numpy as np
# from picamera2 import Picamera2
from copy import deepcopy

try:
    from robohatlib.Robohat import Robohat
    from robohatlib import RobohatConstants
    from robohatlib.hal.assemblyboard.PwmPlug import PwmPlug
    from robohatlib import RobohatConfig
    from robohatlib.hal.assemblyboard.ServoAssemblyConfig import ServoAssemblyConfig
    from robohatlib.hal.assemblyboard.servo.ServoData import ServoData
    from robohatlib.hal.datastructure.Color import Color
    from robohatlib.hal.datastructure.ExpanderDirection import ExpanderDir
    from robohatlib.hal.datastructure.ExpanderStatus import ExpanderStatus
    from robohatlib.driver_ll.datastructs.IOStatus import IOStatus

    from testlib import TestConfig

except ImportError:
    print("Failed to import all dependencies for SerTestClass")
    raise


def start_server():
    server = ZeroMQServer()
    server.listen()

def start_client():
    client = ZeroMQClient()
    client.run()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py [server|client]")
        sys.exit(1)

    role = sys.argv[1].lower()
    if role == "server":
        start_server()
    elif role == "client":
        start_client()
    elif role == "fsm":
        fsm = FSM()
        fsm.search()
    else:
        print("Invalid role. Use 'server' or 'client'.")
        sys.exit(1)