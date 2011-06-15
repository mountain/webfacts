import sys
import os
import rdflib
from os.path import join

g = rdflib.Graph()
errs = []

print "---------------------------------"
print "loading..."
for curdir, subdirs, files in os.walk('./data'):
    for f in files:
        p = join(curdir, f)
        if f.endswith('.n3'):
            print p
            try:
                g.parse(p, format="n3")
            except Exception as err:
                errs.append((p, err))

print "---------------------------------"
print "it loaded " + str(len(g)) + " facts with " + str(len(errs)) + " errors"
for err in errs:
    print "---------------------------------"
    print err[0]
    print err[1]
    print "---------------------------------"

if len(errs) > 0:
    sys.exit(0)

print "---------------------------------"
print "all facts"
for fact in g:
    print "---------------------------------"
    print fact
    print "---------------------------------"

