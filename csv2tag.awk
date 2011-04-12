#! /usr/bin/awk -f
#############################################################################
# csv2tag
#     an awk script to convert a csv file to tag definition n3 file
#
# usage:
#         csv2tag.awk YOURTAGNAME.csv
#
#############################################################################
#
# For below input line
#
# charset,Charset,char encoding of linked resource
#
# It will generate
#
# :charset   a  h:Containment;
#  h:definedIn  s:spec;
#  h:container  t:a;
#  h:containee  a:charset;
#  h:type  t:Charset;
#  rdfs:comment "char encoding of linked resource".
#
#############################################################################

BEGIN {
    FS = ","
    split(ARGV[1], a, ".")
    tag = a[1]
    print "#"
    printf "# data for html4.01 %s tag\n", tag
    print "#"
    print ""
    print "@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>."
    print "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>."
    print "@prefix owl:  <http://www.w3.org/2002/07/owl#>."
    print ""
    print "@prefix h: <../html.n3#>."
    print "@prefix t: <../tags.n3#>."
    print "@prefix a: <../attributes.n3#>."
    print "@prefix p: <../types.n3#>."
    print "@prefix s: <spec.n3#>."
    print ""
    print "@prefix : <#>."
    print ""
    printf ":%s         a            h:Definition;\n", tag
    print "           h:definedIn  s:spec;"
    printf "           h:for        t:%s.\n", tag
}

{
    print ""
    printf ":%s   a            h:Containment;\n", $1
    print "           h:definedIn  s:spec;"
    print "           h:container  t:a;"
    printf "           h:containee  a:%s;\n", $1
    printf "           h:type       t:%s;\n", $2
    printf "           rdfs:comment \"%s\".\n", $3
}
