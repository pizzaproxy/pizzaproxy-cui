#!/usr/bin/env python

import sys
import stfl

if len(sys.argv) <> 2:
    print "Usage: %s stfl-file"%sys.argv[0]
    sys.exit(1)

f=stfl.create("<"+sys.argv[1]+">")

while True:
    try:
        e=f.run(0)
    except KeyboardInterrupt:
        e='^C' 
    if e=='^C':
        break;
    elif e=='ESC':
        break;
