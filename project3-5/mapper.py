#!/usr/bin/python

#The most import thing in this exercise is the way to proccess the entries.
#I used the re module.

import sys
import re
regex = '([\d\.]+) (.+) (.+) \[(.+)\] "([\S]+) ([\S]+) (.+)" (.+) (.+)'

for line in sys.stdin:    
    ma = re.search(regex,str(line))
    data = ma.groups()[5]
    print "{0}\t{1}".format(data,str(1))
