#!/usr/bin/python

import sys
score = [0]*24 #a vector with 24 zeros.
oldUser = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2 or data[0] == "" or data[1] == "": #in case of error
        continue
    user = data[0]
    hour = int(data[1])
    if oldUser and oldUser != user:	#in case of a new user I record the old user
        #print "{0}\t{1}".format(oldUser,score)
        lista = [i for i in range(len(score)) if score[i] == max(score)] #a list with the mosts frequent hours
        for i in lista:
            print "{0}\t{1}".format(oldUser,i)
        score = [0]*24
    oldUser = user
    score[hour] += 1

#To record the last user
if oldUser != None:
    lista = [ i for i in range(len(score)) if score[i] == max(score)]
    for i in lista:
        print "{0}\t{1}".format(oldUser,i)
