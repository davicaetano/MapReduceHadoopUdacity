#!/usr/bin/python

import sys

Counter = 0
oldKey = None
Max = 0
keyMax = None

for line in sys.stdin:
    linevec = line.strip().split("\t")
    thisKey = linevec[0]    
    if oldKey and oldKey != thisKey:
        if Counter > Max:
	    Max = Counter
	    keyMax = oldKey
        Counter = 0

    oldKey = thisKey
    Counter += 1

if oldKey != None:
    if Counter > Max :
	Max = Counter
	keyMax = oldKey
    print "{0}\t{1}".format(keyMax,str(Max))
