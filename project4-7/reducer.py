#!/usr/bin/python

import sys

oldword = None
Count = 0
Nodes = []

for line in sys.stdin:
    linha = line.strip().split("\t")
    word = linha[0]
    nodeid = int(linha[1])
    if oldword and oldword != word:
        Nodes.sort()
        print "{0}\t{1}\t{2}".format(oldword,len(Nodes),Nodes)
        Count = 0
        Nodes = []
    oldword = word
    Count += 1
    #if len(Nodes) < 5: #This is a limit to the index's length. Use this line only if your code is nothing work well
    if 1:
        if not(nodeid in Nodes):
            Nodes.append(nodeid)

if oldword != None:
    Nodes.sort()
    print "{0}\t{1}\t{2}".format(oldword,len(Nodes),Nodes)
