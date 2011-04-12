import os
import rdflib
from os.path import join

g = rdflib.Graph()
errs = []

for curdir, subdirs, files in os.walk('./'):
    for f in files:
        p = join(curdir, f)
        if f.endswith('.n3'):
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

