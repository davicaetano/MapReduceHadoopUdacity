#!/usr/bin/python

import sys

salesTotal = 0
countTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", str(salesTotal/countTotal)
        oldKey = thisKey;
        salesTotal = 0
        countTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)
    countTotal += 1

if oldKey != None:
    print oldKey, "\t", str(salesTotal/countTotal)
