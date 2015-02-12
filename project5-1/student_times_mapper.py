#!/usr/bin/python

import sys
from datetime import datetime
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

for line in reader:
    user = line[3].strip("\"") #To get the user id
    if user != "author_id":
		#I use the method hour on the line[8].
        hour = datetime.strptime(re.search("([\-\d\:\s]+)",line[8]).group(), "%Y-%m-%d %H:%M:%S").hour
        writer.writerow([user,hour])
