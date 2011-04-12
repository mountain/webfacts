#!/usr/bin/env python

import sys
import rdflib

if len(sys.argv) == 0:
     sys.exit(0)

g = rdflib.Graph()

try:
    g.parse(sys.argv[1], format="n3")
except Exception as err:
    print err

for stmt in g:
    print stmt
