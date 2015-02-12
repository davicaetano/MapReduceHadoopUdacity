#!/usr/bin/python

import sys
oldpostid = None
lista = []

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    postid = data[0]
    authorid = int(data[1])
    if oldpostid and oldpostid != postid:#when we have a new postid we print the old
        lista.sort()#order the list
        print "{0}\t{1}".format(oldpostid,lista)
        lista = []

    oldpostid = postid
    lista.append(authorid)

#print the last one
if oldpostid != None:
    lista.sort()
    print "{0}\t{1}".format(oldpostid,lista)
