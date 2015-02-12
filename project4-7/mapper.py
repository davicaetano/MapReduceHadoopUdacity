#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
for node in reader:

    nodeid = node[0].strip("\"")
    body = node[4].strip("\"")
    body = re.sub('[^a-zA-Z]+',' ',body).lower() #ignore everything that is not letters. Numbers, points and other caracteres.
    body = re.sub(' +',' ',body) #replace all multiple spaces with single space.
    body = body.split(" ")
    if nodeid != "id":
        for word in body:
            if word != " " and word != "":
                print "{0}\t{1}".format(word,nodeid)
