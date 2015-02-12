#!/usr/bin/python

import sys
import re
regex = '([\d\.]+) (.+) (.+) \[(.+)\] "([\S]+) ([\S]+) (.+)" (.+) (.+)'

for line in sys.stdin:    
    ma = re.search(regex,str(line))
    data = ma.groups()[5]
    if data[0:len("http://www.the-associates.co.uk")] == "http://www.the-associates.co.uk":
        data = data[31:]
    print "{0}\t{1}".format(data,str(1))
