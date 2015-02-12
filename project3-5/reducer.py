#!/usr/bin/python

import sys

Counter = 0
oldKey = None

for line in sys.stdin:
    newKey = line.strip().split("\t")[0]
    if oldKey and oldKey != newKey:
        print "{0}\t{1}".format(oldKey,Counter)
        Counter = 0
    oldKey = newKey
    Counter += 1

if oldKey != None:
    print "{0}\t{1}".format(oldKey,Counter)
