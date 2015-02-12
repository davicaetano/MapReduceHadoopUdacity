#!/usr/bin/python

import sys

oldword = None
Nodes = {}

for line in sys.stdin:
    linha = line.strip().split("\t")
    word = linha[0]
    nodeid = int(linha[1])
    position = int(linha[2])
    if oldword and oldword != word:
        #sort dictionary
        a = Nodes.items()
        a.sort() #sorting the posts where the word is present
        for i in range(len(a)):
            if len(a[i][1]) >1:
                a[i][1].sort() #sorting the positions in a same post
        print "{0}\t{1}\t{2}".format(oldword,len(a),a)
        Nodes = {}
    oldword = word
    
    #if len(Nodes) <= 5: #This is a limit to the index's length. Use this line only if your code is nothing work well
    if 1:
        if nodeid in Nodes.keys(): #if is present, append. else, create a new vector with positions.
            Nodes[nodeid].append(position)
        else:
            Nodes[nodeid] = [position]

#to print the last record
if oldword != None:
    a = Nodes.items()
    a.sort()
    for i in range(len(a)):
        if len(a[i][1]) >1:
            a[i][1].sort()
    print "{0}\t{1}\t{2}".format(oldword,len(a),a)
