#!/usr/bin/env python
import subprocess
import sys
import urllib.parse


# Enter the path to your UrT executable
URT_EXECUTABLE = "~/UrbanTerror42/Quake4-UrT.i386"


url = urllib.parse.urlparse(sys.argv[1])
arg = [URT_EXECUTABLE, "+connect", url.netloc]

qs = urllib.parse.parse_qsl(url.query)
for kv in qs:
    arg.append("+" + kv[0])
    arg.append(kv[1])

subprocess.call(arg)

