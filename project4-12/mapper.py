#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

for line in reader:
    if not(line[0] in ["id","user_ptr_id"]):
        if len(line) == 5:
            saida = []
            saida.append(line[0])
            saida.append("A")
            saida.extend(line[1:])
            
        else:
            saida = []
            saida.append(line[3])
            saida.append("B")
            saida.extend(line[0:3])
            saida.extend(line[5:])
        writer.writerow(saida)
