#!/usr/bin/python

import sys

salesNumber = 0.0
salesTotal = 0.0

for line in sys.stdin:
    data = line.strip().split("\t")
    thisSale = float(data[0])
    salesNumber += 1
    salesTotal += thisSale

print "Sales Total\t",salesTotal
print "Sales Number\t",salesNumber
