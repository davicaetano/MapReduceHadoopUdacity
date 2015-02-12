#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

for line in reader:
    postid = line[0].strip("\"")
    tags = line[2].strip("\"").split(" ")
    if postid != "id": #don't print the first line
        for tag in tags: #print all tags
            if tag != "": #don't print empty tags
                writer.writerow([tag,1])
