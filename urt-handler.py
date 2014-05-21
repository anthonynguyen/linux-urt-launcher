#!/usr/bin/env python
import subprocess
import sys
import urlparse


# Enter the path to your UrT executable
URT_EXECUTABLE = "/home/clearskies/UrbanTerror42/Quake3-UrT.i386"


url = urlparse.urlparse(sys.argv[1])
arg = [URT_EXECUTABLE, "+connect", url.netloc]

qs = urlparse.parse_qsl(url.query)
for kv in qs:
	arg.append("+" + kv[0])
	arg.append(kv[1])

subprocess.call(arg)
