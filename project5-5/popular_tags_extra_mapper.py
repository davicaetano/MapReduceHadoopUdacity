#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

for line in reader:
    postid = line[0].strip("\"")
    tags = line[2].strip("\"").split(" ")
    typeid = line[5].strip("\"")
    if postid != "id": #don't print the first line
        value = 1
        if typeid == "question":#if is a question, the weigth is 2. otherwise, 1.
            value = 2
        for tag in tags: #print all tags
            if tag != "": #don't print empty tags
                writer.writerow([tag,value])
