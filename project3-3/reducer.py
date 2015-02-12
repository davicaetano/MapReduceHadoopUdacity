#!/usr/bin/python

import sys

salesMax = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesMax
        salesMax = 0

    oldKey = thisKey
    salesMax = max(salesMax,float(thisSale))

if oldKey != None:
    print oldKey, "\t", salesMax
