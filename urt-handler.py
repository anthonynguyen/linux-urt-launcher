#!/usr/bin/env python
import subprocess
import sys


# Enter the path to your UrT executable
URT_EXECUTABLE = "/home/clearskies/UrbanTerror42/Quake3-UrT.i386"


subprocess.call([URT_EXECUTABLE, "+connect", sys.argv[1][6:]])
