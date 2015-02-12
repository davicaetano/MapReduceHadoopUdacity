#!/usr/bin/python

import sys
oldtag = None
top10 = {} #a dictionaty to save the top ten tags with the number them were used.
counter = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    tag = data[0]
    value = int(data[1])
    if oldtag and oldtag != tag: #in case of a new tag i do smt with the old tag
        if len(top10.keys())<10:#if the dic don't have 10 tags, i add the tag
            top10[oldtag] = counter
        else:#if there are 10 tags in the dict i replace only if he is more frequent than the min frequency
            if counter > min(top10.values()):
                for tf,ct in top10.items():
                    if ct == min(top10.values()):
                        del top10[tf]
                        top10[oldtag] = counter
                        break #i just replace one of the mins values.
        #zera
        counter = 0

    oldtag = tag
    counter += value

#the last tag, the same proccess
if len(top10.keys())<10:
    top10[oldtag] = counter
else:
    if counter > min(top10.values()):
        for tf,ct in top10.items():
            if ct == min(top10.values()):
                del top10[tf]
                top10[oldtag] = counter
                break

#First i order the dictionary. 
a = top10.items()
a = [[j[1],j[0]]for j in a]
a.sort()
#Then I print it.
for i in range(len(top10.items())-1,-1,-1):
    print "{0}\t{1}".format(a[i][1],a[i][0])
