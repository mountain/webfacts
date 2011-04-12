import os
import sys
import rdflib
import urllib
from urlparse import urljoin
from os.path import join
from string import Template

rdflib.plugin.register('sparql', rdflib.query.Processor,
                       'rdfextras.sparql.processor', 'Processor')
rdflib.plugin.register('sparql', rdflib.query.Result,
                       'rdfextras.sparql.query', 'SPARQLQueryResult')

g = rdflib.Graph()
errs = []

print "---------------------------------"
print "loading..."
for curdir, subdirs, files in os.walk('./'):
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

if len(err) > 0:
    sys.exit(0)

if len(sys.argv) == 0:
     sys.exit(0)

f = open(sys.argv[1])
q = ""
for ln in f.readlines():
    q = q + ln

env = {"base": urljoin("file:///", urllib.pathname2url(os.path.abspath("./")))}
q = Template(q).safe_substitute(env)

ns = {}
try:
    ns["xsd"] = rdflib.XSD
    ns["rdf"] = rdflib.RDF
    ns["rdfs"]= rdflib.RDFS
    ns["owl"] = rdflib.OWL
except Exception as err:
    print err

result = []
try:
    result = g.query(q, initNs=ns)
except Exception as err:
    print err

print "---------------------------------"
print q
print "---------------------------------"
print "query result..."
for row in result:
    print "---------------------------------"
    print row
print "---------------------------------"

