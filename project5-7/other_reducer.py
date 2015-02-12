#!/usr/bin/python

import sys
oldUser = None
scores = []

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2 or data[0] == "" or data[1] == "": #in case of error
        continue
    user = data[0]
    score = int(data[1])
    if oldUser and oldUser != user:	#in case of a new user I record the old user
        print "{0}\t{1}\t{2}\t{3}\t{4}".format(oldUser,len(scores),1.0*sum(scores)/len(scores),min(scores),max(scores))
        scores = []
    oldUser = user
    scores.append(score)

#To record the last user
if oldUser != None:
    print "{0}\t{1}\t{2}\t{3}\t{4}".format(oldUser,len(scores),1.0*sum(scores)/len(scores),min(scores),max(scores))

