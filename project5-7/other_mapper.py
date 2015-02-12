#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

for line in reader:
    user = line[3].strip("\"") #To get the user id
    score = line[9].strip("\"") #To get the user score
    if user != "author_id":
        writer.writerow([user,score])
