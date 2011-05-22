#!/usr/bin/env python

import os
import sys

import id3

if len(sys.argv) < 2:
    print "Usage: %s <filename>" % os.path.basename(sys.argv[0])
    sys.exit(0)

filename = sys.argv[0]
id3.showInfo(filename)
