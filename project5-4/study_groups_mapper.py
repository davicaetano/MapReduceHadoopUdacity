#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

for line in reader:
    postid = line[0].strip("\"")
    parentid = line[7].strip("\"")
    authorid = line[3].strip("\"")
    typeid = line[5].strip("\"")
    if postid != "id":
        if typeid == "question":#if is a quetion, print the postid, else print the parentid
            writer.writerow([postid,authorid])
        else:
            writer.writerow([parentid,authorid])
