#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

for line in reader:
    postid = line[0].strip("\"") #postid
    parentid = line[7].strip("\"") #parent_id
    typeid = line[5].strip("\"") #type_id
    length = len(line[4]) #lenght
    if postid != "id": #to don't use the first line
        if typeid == "question": #if is question, use the postid. else, the parentid
            writer.writerow([postid,1,length])
        else:
            writer.writerow([parentid,2,length])
