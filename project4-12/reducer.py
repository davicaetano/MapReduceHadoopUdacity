#!/usr/bin/python

import sys
import csv
user = None
base = []
writer = csv.writer(sys.stdout, delimiter='\t',quotechar='"', quoting=csv.QUOTE_ALL)

for line in sys.stdin:
    dados = line.strip().split("\t")
    if user and user != dados[0]:
        #grava
        for post in base:
            saida = []
            saida.extend(post)
            saida.extend(dadosuser)
            writer.writerow(saida)
        base = []
    user = dados[0]
    if dados[1] == "A":
        dadosuser = dados[2:6]
    else:
        base.append(dados[2:])

for post in dados:
    saida = []
    saida.extend(post)
    saida.extend(dadosuser)
    writer.writerow(saida)
