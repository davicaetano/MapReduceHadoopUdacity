#!/usr/bin/python

import sys
oldpostid = None
total = 0
count = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 3: #in case of error
        continue
    postid = data[0] 
    typeid = data[1]
    lenght = int(data[2])
    if oldpostid and oldpostid != postid: #in case of a new postid, print the last
        print "{0}\t{1}\t{2}".format(oldpostid,parentlength,(total*1.0/count if count>0 else 0))
        total = 0
        count = 0

    oldpostid = postid
    if typeid == "1": #if typeid is 1, this is the parent post. else, this is an answer
        parentlength = lenght
    else:
        total += lenght
        count += 1

#To post the last one
if oldpostid != None:
    print "{0}\t{1}\t{2}".format(oldpostid,parentlength,(total/count if count>0 else 0))
